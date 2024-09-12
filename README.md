# Web Scraping Project: Extract Text and Image from a Webpage

This project demonstrates how to scrape text data and download images from a webpage using Python. The scraped text is saved to an Excel file, and a specific image is downloaded and saved locally. 

## Features

- Scrapes paragraph text (`<p>`) and headers (`<h2>`) from a given webpage.
- Saves the extracted text data into an Excel file using `pandas` and `xlsxwriter`.
- Downloads a specific image from a given URL and saves it to a local directory.

## Prerequisites

To run this project, you need the following libraries installed:

- `requests` (for sending HTTP requests)
- `beautifulsoup4` (for parsing HTML)
- `pandas` (for handling data and saving it to an Excel file)
- `xlsxwriter` (for generating Excel files)
- `os` (for file and directory handling)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danukarangith/web-scraping-image-text.git
   cd web-scraping-image-text
 
### Install the required dependencies

pip install requests beautifulsoup4 pandas xlsxwriter
