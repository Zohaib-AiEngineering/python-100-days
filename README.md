# Lead Scraper

## Description
This project is a simple web scraper built with python.
It extracts product information and stores it in an Excel file.
## Features
- **HTML Parsing**: Extracts product titles, prices, and links using `BeautifulSoup`.
- **Data Cleansing**: Cleans price strings by removing currency symbols (`$`) and whitespace, converting values into proper numeric data types (`int`).
- **Pandas Data Pipeline**: Organizes scraped items into a structured Pandas DataFrame.
- **Automated Export**: Automatically exports cleaned data directly into Excel (`.xlsx`) and CSV formats.