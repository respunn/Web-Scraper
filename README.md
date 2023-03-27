# Web Scraper

This is a Python script that downloads the HTML, CSS, and images of a website using the `requests` and `BeautifulSoup` libraries. It prompts the user to enter a website URL, then extracts the domain name from the URL and creates a directory with that name to store the downloaded files.

## Requirements

To run this script, you need to have Python 3 installed on your computer, as well as the following Python libraries:

- requests
- BeautifulSoup

You can install these libraries using pip by running the following command in your terminal:

```bash
pip install requests beautifulsoup4
```

## How to use

1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the directory where you cloned this repository.
3. Run the script by running the following command in your terminal:

`python web_scraper.py`

4. Enter the URL of the website you want to download. You can exit the script by typing `exit`.

## Code explanation

- The script starts by importing the necessary libraries and defining some variables, such as the directory of the script file (`script_dir`).

- It then enters a loop that prompts the user to enter a website URL. If the user enters "exit", the loop breaks and the script ends.

- If the user enters a valid URL, the script sends a GET request to that URL using the `requests` library.

- If the request is successful, the script uses `BeautifulSoup` to parse the HTML content of the website.

- The script then extracts the domain name from the URL and creates a directory with that name to store the downloaded files.

- If the directory already exists, the script deletes it first to avoid overwriting existing files.

- The script then creates a subdirectory called "images" to store the downloaded images.

- The HTML content of the website is saved to a file called "index.html" in the main directory.

- The script then loops through all the `<img>` tags in the HTML and downloads the images to the "images" directory.

- The filename of each image is the last part of its URL (i.e. the part after the last "/").

- If there is an error in the process of downloading the website, an exception is raised and the script prints an error message.

- When the script finishes downloading the website, it prints a success message.

## Conclusion

This script provides a simple way to download the HTML, CSS, and images of a website using Python. It can be useful for various purposes, such as offline browsing or web scraping. However, please note that downloading a website without permission is illegal in some cases, so use this script responsibly.
