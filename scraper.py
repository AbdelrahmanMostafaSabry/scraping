"""
Books to Scrape Web Scraper
Scrapes all books from https://books.toscrape.com/
Saves data as CSV and JSON
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import time
import csv
import json

# ------------------------------
# Initialization
# ------------------------------
booksList = []  # List to store all books
Base_Url = 'https://books.toscrape.com/'  # Starting page
start_time = time.time()  # Track runtime

# ------------------------------
# Scraping loop (all pages)
# ------------------------------
while Base_Url:

    # Request page content
    Response = requests.get(Base_Url)
    Response.encoding = 'utf-8'  # Fix special characters
    Soup = BeautifulSoup(Response.text, 'html.parser')

    # Find all books on the page
    Books = Soup.find_all('article', class_='product_pod')

    # Extract data for each book
    for article in Books:
        title = article.h3.a['title']  # Book title
        rating = article.find('p', class_='star-rating')['class'][1]  # Rating (One, Two...)
        price = article.find('p', class_='price_color').text  # Price with £
        availability = article.find('p', class_='instock availability').get_text(strip=True)  # Stock info
        relative_url = article.find('a')['href']  # Book page relative URL
        book_url = urljoin(Base_Url, relative_url)  # Convert to absolute URL

        # Create a dictionary for the book
        book_data = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Url": book_url,
        }

        # Append to the main list
        booksList.append(book_data)

    # Check for next page
    next_page = Soup.find('li', class_='next')
    if next_page:
        Base_Url = urljoin(Base_Url, next_page.find('a')['href'])
        time.sleep(1)  # Optional delay to be polite with server
    else:
        Base_Url = None  # Stop loop if no next page

# ------------------------------
# Save data to JSON
# ------------------------------
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(booksList, f, ensure_ascii=False, indent=4)
    
print("books.json saved successfully!")

# ------------------------------
# Save data to CSV
# ------------------------------
with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Price', 'Rating', 'Availability', 'Url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Column headers
    for book in booksList:
        writer.writerow(book)

print("books.csv saved successfully!")

# ------------------------------
# Print runtime
# ------------------------------
end_time = time.time()
print(f"Runtime: {end_time - start_time:.2f} seconds")
print(f"Total books scraped: {len(booksList)}")
