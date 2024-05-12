import time
import re
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


def scrape_website(url, visited=None, base_url='https://developer.apple.com', max_links=50):
    if visited is None:
        visited = set()

    if url in visited:
        return

    visited.add(url)

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
            title = re.sub('[^\w\s-]', '', soup.title.text).strip().replace(' ', '_')
            content = content_div.get_text(separator='\n')
            save_to_markdown(f'# {title}\n{content}', f'{title}.md')

        child_links = [base_url + link.get('href') for link in soup.find_all('a', href=True)
                       if link.get('href').startswith('/documentation/shadergraph') and '#' not in link.get('href')
                       and base_url + link.get('href') not in visited and base_url + link.get(
                'href') not in load_child_links()]

        save_child_links(child_links)

        for child_link in child_links:
            scrape_website(child_link, visited, base_url, max_links)

    except Exception as e:
        print(f"Error while scraping {url}: {str(e)}")
        save_to_markdown('Error encountered', f'error_{url[-30:]}.md')  # Save errors with a unique identifier


def save_to_markdown(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Content from {filename} has been saved.")


def scrape_loaded_links(base_url='https://developer.apple.com', max_links=200):
    os.makedirs('Documentation', exist_ok=True)  # Ensure the Documentation directory exists
    visited = load_child_links()  # Load all previously stored links

    for url in list(visited)[:max_links]:  # Limit the number of links to scrape in one run if needed
        try:
            title = re.sub('[^\w\s-]', '', url.split('/')[-1]).strip().replace(' ', '_')  # Generate title based on URL
            if os.path.exists(f'Documentation/{title}.md'):
                print(f"Skipping Documentation/{title}.md as it already exists.")
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
                save_to_markdown(f'# {title}\n{content}', f'Documentation/{title}.md')

        except Exception as e:
            print(f"Error while scraping {url}: {str(e)}")
            error_filename = f'Documentation/error_{title}.md'
            save_to_markdown('Error encountered', error_filename)

def save_child_links(child_links):
    existing_links = load_child_links()
    existing_links.update(set(child_links))
    with open('child_links.pkl', 'wb') as file:
        pickle.dump(existing_links, file)


def load_child_links():
    if os.path.exists('child_links.pkl'):
        with open('child_links.pkl', 'rb') as file:
            return pickle.load(file)
    return set()


def save_to_markdown(content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Content from {filename} has been saved.")


def save_child_links(child_links):
    existing_links = load_child_links()
    existing_links.update(child_links)
    with open('child_links.pkl', 'wb') as file:
        pickle.dump(existing_links, file)


initial_url = 'https://developer.apple.com/documentation/shadergraph'
scraped_content = scrape_website(initial_url)


def print_child_links():
    if os.path.exists('child_links.pkl'):
        with open('child_links.pkl', 'rb') as file:
            links = pickle.load(file)
            print("Child Links:")
            for link in links:
                print(link)
    else:
        print("No child links file found.")


# Call this function to print the child links
print_child_links()

# if scraped_content:
#     save_to_markdown(scraped_content, 'scraped_content.md')
scrape_loaded_links(base_url=initial_url, max_links=200)
