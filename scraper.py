import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def scrape_website(url, visited=None, scraped_content=None):
    if visited is None:
        visited = set()
    if scraped_content is None:
        scraped_content = []

    if url in visited:
        return

    visited.add(url)

    # Set up Selenium webdriver
    service = Service('/opt/homebrew/bin/chromedriver')  # Replace with the path to your webdriver executable
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(1)  # Wait for 5 seconds before scraping the page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    content_div = soup.find('div', {'data-v-2016a34c': True, 'class': 'content'})
    if content_div:
        title = soup.title.text
        content = content_div.get_text(separator='\n')

        scraped_content.append(f'# {title}\n')
        scraped_content.append(content)
        scraped_content.append('\n---\n')

    child_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/documentation/shadergraph'):
            child_link = 'https://developer.apple.com' + href
            child_links.append(child_link)

    for child_link in child_links:
        scrape_website(child_link, visited, scraped_content)

    return scraped_content

def save_to_markdown(content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n'.join(content))

initial_url = 'https://developer.apple.com/documentation/shadergraph'
scraped_content = scrape_website(initial_url)

save_to_markdown(scraped_content, 'scraped_content.md')
print("Markdown file generated successfully!")