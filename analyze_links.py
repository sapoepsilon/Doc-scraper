import pickle
import os

base_url = input("Please enter the parent URL for the documentation you are trying to scrape to analyze it : ")

# Load the links from child_links.pkl
with open("child_links.pkl", "rb") as f:
    links = pickle.load(f)
    print("Scrappable links amount: " + str(len(links)))

# Get all files in the documentation directory
documentation_files = []
for root, dirs, files in os.walk("documentation/documentation"):
    for file in files:
        if file.endswith(".md"):
            documentation_files.append(os.path.join(root, file))

# Extract the base names of the documentation files
scraped_links = set()
if not base_url.endswith('/'):
    base_url += '/'

print("Documentation files amount: " + str(len(documentation_files)))
print("base_url: " + base_url)
for file in documentation_files:
    base_name = file.replace("documentation/", "").replace(".md", "")
    base_name = base_url + base_name
    scraped_links.add(base_name)

# Calculate the count of scraped and not scraped links
scraped_count = sum(1 for link in links if link in scraped_links)
not_scraped_count = len(links) - scraped_count

# Output the results in a table format
print("\033[1mStatus\033[0m\t\033[1mCount\033[0m")
print(f"\033[32mScraped\033[0m\t\033[32m{scraped_count}\033[0m")
print(f"\033[31mMissing\033[0m\t\033[31m{not_scraped_count}\033[0m")
