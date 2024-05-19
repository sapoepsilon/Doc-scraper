import time
import re
import os
import pickle
import logging
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s - [%(lineno)d]')

def clean_url(url, base_url):
    """Ensure the URL is correctly formed and relative to the base URL."""
    return urljoin(base_url, url) if url.startswith('/') else url

def scrape_website(url, visited=None, base_url='https://developer.apple.com', max_links=50):
    if visited is None:
        visited = set()

    if url in visited:
        return

    visited.add(url)
    logging.info(f"Visiting: {url}")

    try:
        # Set up Selenium webdriver
        service = Service('/opt/homebrew/bin/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        time.sleep(1)  # Adjust sleep as necessary for page load
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        content_div = soup.find('div', {'data-v-2016a34c': True, 'class': 'content'})
        if content_div:
            title = get_title_from_url(url)
            save_path = f'{get_save_path(url)}.md'
            if os.path.exists(save_path):
                logging.info(f"Skipping {save_path} as it already exists.")
            else:
                content = content_div.get_text(separator='\n')
                save_to_markdown(f'# {title}\n{content}', save_path)

            # Find new child links
            new_child_links = [clean_url(link.get('href'), base_url) for link in soup.find_all('a', href=True)
                               if link.get('href').startswith('/documentation/shadergraph') and '#' not in link.get('href')
                               and clean_url(link.get('href'), base_url) not in visited]

            # Save only new child links
            save_child_links(new_child_links)
            visited.update(new_child_links)  # Update visited with new links

        for child_link in new_child_links:
            scrape_website(child_link, visited, base_url, max_links)

    except Exception as e:
        logging.error(f"Error while scraping {url}: {str(e)}")
        save_to_markdown('Error encountered', f'{get_save_path(url)}_error.md')  # Save errors with a unique identifier

def save_to_markdown(content, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # Ensure the directory exists
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    logging.info(f"Content from {filename} has been saved.")

def get_save_path(url):
    path_parts = url.rstrip('/').split('/')[3:-1]  # Split the URL and remove the base URL part
    save_directory = os.path.join(*path_parts)
    filename = url.rstrip('/').split('/')[-1]
    return os.path.join(save_directory, filename)  # Join parts into a directory path with filename

def get_title_from_url(url):
    return re.sub('[^\w\s-]', '', url.split('/')[-1]).strip().replace(' ', '_')

def scrape_loaded_links(base_url='https://developer.apple.com', max_links=200):
    visited = load_child_links()  # Load all previously stored links

    for url in list(visited)[:max_links]:  # Limit the number of links to scrape in one run if needed
        try:
            title = get_title_from_url(url)
            save_path = get_save_path(url)
            if os.path.exists(f'{save_path}.md'):
                logging.info(f"Skipping {save_path}.md as it already exists.")
                continue

            service = Service('/opt/homebrew/bin/chromedriver')
            driver = webdriver.Chrome(service=service)
            driver.get(url)
            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            driver.quit()

            content_div = soup.find('div', {'data-v-2016a34c': True, 'class': 'content'})
            if content_div:
                content = content_div.get_text(separator='\n')
                save_to_markdown(f'# {title}\n{content}', f'{save_path}.md')

                # Find new child links
                new_child_links = [clean_url(link.get('href'), base_url) for link in soup.find_all('a', href=True)
                                   if link.get('href').startswith('/documentation/shadergraph') and '#' not in link.get('href')
                                   and clean_url(link.get('href'), base_url) not in visited]

                # Save only new child links
                save_child_links(new_child_links)
                visited.update(new_child_links)  # Update visited with new links

        except Exception as e:
            logging.error(f"Error while scraping {url}: {str(e)}")
            error_filename = f'{save_path}_error.md'
            save_to_markdown('Error encountered', error_filename)

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

initial_url = 'https://developer.apple.com/documentation/shadergraph'
scrape_website(initial_url)

# Call this function to print the child links
print_child_links()

scrape_loaded_links(base_url=initial_url, max_links=200)
