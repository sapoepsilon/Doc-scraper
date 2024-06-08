# Documentation Web Scraper

This Python script automates the process of scraping web pages for documentation and saving the content in Markdown format. It uses Selenium for web browsing and BeautifulSoup for parsing HTML content.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- [Chrome browser](https://www.google.com/chrome/browser-tools/)

## Usage
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Running the Script
`python3 scraper.py`

`python analyze_link` - will analyze scraped docs, make sure to give a parent url.