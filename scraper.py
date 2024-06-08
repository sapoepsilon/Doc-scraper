import time
import re
import os
import pickle
import logging
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s - [%(lineno)d]')

def clean_url(url, base_url):
    """Ensure the URL is correctly formed and relative to the base URL."""
    return urljoin(base_url, url) if url.startswith('/') else url

def get_save_path(url):
    path_parts = url.rstrip('/').split('/')[3:-1]  # Split the URL and remove the base URL part
    save_directory = os.path.join('documentation', *path_parts)
    filename = url.rstrip('/').split('/')[-1]
    return os.path.join(save_directory, filename)

def scrape_website(url, visited=None, base_url='https://developer.apple.com', max_links=50):
    save_path = get_save_path(url)
    if not save_path.endswith('.md'):
        save_path += '.md'

    if visited is None:
        visited = set()

    if url in visited:
        return

    # if os.path.exists(save_path):
    #     logging.info(f"Skipping {save_path} befre scraping as it already exists.")
    #     return
    else:
        logging.info(f"Did not find {save_path} in the file system.")

    visited.add(url)
    logging.info(f"Visiting: {url}")

    try:
        service = Service('/opt/homebrew/bin/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        time.sleep(1)  # Adjust sleep as necessary for page load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        body_div = soup.find('div', {'data-v-3c25fba5': True, 'class': 'primary-content with-border'})
        see_also_div = soup.find('div', {'data-v-c26e77ea': True, 'class': 'container'})
        content_div = soup.find('div', {'data-v-15d7e6ba': True, 'class': 'content'})

        if body_div or see_also_div or content_div:
            title = get_title_from_url(url)
            save_path = f'{get_save_path(url)}.md'
            if os.path.exists(save_path):
                logging.info(f"Skipping {save_path} as it already exists.")
            else:
                content = ""
                if body_div:
                    content += body_div.prettify()
                if content_div:
                    content += content_div.prettify()

                markdown_options = {
                    'strip': ['style'],
                    'autolinks': False,
                    'wrap': 80,
                    'bold_mark': '**',
                    'italic_mark': '*',
                    'table_conversion': {
                        'thead_tr_format': '| {} |',
                        'thead_th_format': ' **{}** |',
                        'tbody_tr_format': '| {} |',
                        'tbody_td_format': ' {} |',
                    }
                }
                markdown_content = md(content, options=markdown_options)
                markdown_content = re.sub(r'\n{3,}', '\n\n',
                                          markdown_content)
                if see_also_div:
                    markdown_content += md(see_also_div.prettify(),
                                           options=markdown_options)
                    markdown_content = re.sub(r'\n{3,}', '\n\n',
                                              markdown_content)
                save_to_markdown(f'# {title}\n{markdown_content}', save_path)

                logging.info(f"Scraped content for {url}")

        # Find new child links
        new_child_links = [clean_url(link.get('href'), base_url) for link in soup.find_all('a', href=True)
                           if link.get('href').startswith('/documentation/shadergraph') and '#' not in link.get('href')
                           and clean_url(link.get('href'), base_url) not in visited]

        if new_child_links:
            save_child_links(new_child_links)
            visited.update(new_child_links)  # Update visited with new links
            logging.info(f"New child links found and saved for {url}")

        for child_link in new_child_links:
            if len(visited) < max_links:
                scrape_website(child_link, visited, base_url, max_links)

    except Exception as e:
        logging.error(f"Error while scraping {url}: {str(e)}")
        save_to_markdown('Error encountered', f'{get_save_path(url)}_error.md')  # Save errors with a unique identifier

def save_to_markdown(content, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure the directory exists
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    logging.info(f"Content from {filename} has been saved.")

def get_title_from_url(url):
    return re.sub(r'[^\w\s-]', '', url.split('/')[-1]).strip().replace(' ', '_')

def get_base_path(url, depth=2):
    """
    Extracts a base path from a URL up to a specified depth.
    Example: "http://example.com/doc/shadergraph/last_work" with depth=2 would return '/doc/shadergraph'.
    """
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.strip('/').split('/')  # Split path into segments and remove any leading/trailing slashes
    base_path = '/' + '/'.join(path_segments[:depth])  # Join the required number of segments
    return base_path

def scrape_loaded_links(base_url, max_links=200):
    visited = load_child_links()

    for url in list(visited)[:max_links]:  # Limit the number of links to scrape in one run if needed
        scrape_website(url)

def save_child_links(child_links):
    existing_links = load_child_links()
    new_links = set(child_links) - existing_links  # Only keep new links
    if new_links:
        existing_links.update(new_links)
        with open('child_links.pkl', 'wb') as file:
            pickle.dump(existing_links, file)
        logging.info(f"New links saved: {new_links}")

def load_child_links():
    if os.path.exists('child_links.pkl'):
        with open('child_links.pkl', 'rb') as file:
            return pickle.load(file)
    return set()

def print_child_links():
    if os.path.exists('child_links.pkl'):
        with open('child_links.pkl', 'rb') as file:
            links = pickle.load(file)
            logging.info("Child Links:")
            for link in links:
                logging.info(link)
    else:
        logging.info("No child links file found.")

initial_url = input("Please enter the initial URL to scrape: ")
scrape_website(initial_url)
base_path = get_base_path(initial_url, depth=2)  # Adjust 'depth' as needed based on URL structure

# Call this function to print the child links
print_child_links()

scrape_loaded_links(base_url=initial_url, max_links=200)
