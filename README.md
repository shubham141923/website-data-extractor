Website Data Extractor
=====================

This repository contains a Python script that extracts images data, font families, color tags, and heading tags information from a given website URL.

**Usage:**

1. Clone the repository: `git clone https://github.com/shubham141923/website-data-extractor.git`
2. Install the required packages: `pip install requests beautifulsoup4`
3. Run the script: `python extract_website_data.py <website_url>`

**Example:**

`python extract_website_data.py [https://www.w3schools.com/html/]`

**Output:**

The script will print the extracted data to the console, including:

* Images data (src and alt attributes)
* Font families used on the website
* Color tags used on the website
* Heading tags information (h1-h6)

**Documentation:**

The script uses the `requests` and `beautifulsoup4` libraries to fetch the HTML content of the website and parse it. The extracted data is stored in a dictionary and returned at the end of the script.

You can modify the script to suit your needs and add more functionality as required.
