# Books to Scrape - Web Scraper

This project scrapes all books from [Books to Scrape](https://books.toscrape.com/) and saves the data as CSV and JSON files.

## Features
- Scrapes all book pages automatically (pagination supported)
- Extracts:
  - Title
  - Price
  - Rating
  - Availability
  - Book URL
- Saves data as `books.csv` and `books.json`
- Measures runtime for performance tracking
- Polite scraping with small delay between pages

## How to Run
1. Clone this repository:
```bash
git clone https://github.com/AbdelrahmanMostafaSabry/books_scraper.git

2. pip install -r requirements.txt

3. python scraper.py => RUN

4.output => books.csv , books.json


