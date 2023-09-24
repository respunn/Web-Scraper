import requests
from bs4 import BeautifulSoup
import os
import shutil
from urllib.parse import urlparse, urljoin

# Get the directory of the script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Keep prompting user for website URL until they type "exit"
while True:
    url = input("Enter the URL of the website you want to download (or 'exit' to quit): ")

    if url == "exit":
        break

    try:
        # Send a GET request to the URL and get the response
        response = requests.get(url)

        # Parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract domain name from URL and create a directory with that name to store the HTML and CSS files
        domain_name = urlparse(url).netloc
        output_folder = os.path.join(script_dir, 'output', domain_name)

        # Delete the old folder if it exists
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)

        # Create a new folder
        os.makedirs(output_folder)

        # Create a directory to store the images
        images_folder = os.path.join(output_folder, 'images')
        os.makedirs(images_folder, exist_ok=True)

        # Create a directory to store the JavaScript files
        js_folder = os.path.join(output_folder, 'js')
        os.makedirs(js_folder, exist_ok=True)

        # Save the HTML code to a file
        html_content = str(soup)
        with open(os.path.join(output_folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

        # Save the images to files
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                img_url = urljoin(url, src)
                img_content = requests.get(img_url).content
                filename = os.path.join(images_folder, src.split('/')[-1])
                with open(filename, 'wb') as f:
                    f.write(img_content)

        # Save the JavaScript files to disk
        for script in soup.find_all('script'):
            src = script.get('src')
            if src:
                js_url = urljoin(url, src)
                js_content = requests.get(js_url).content
                filename = os.path.join(js_folder, src.split('/')[-1])
                with open(filename, 'wb') as f:
                    f.write(js_content)

        # Print a success message after saving the files
        print("HTML, CSS, and images saved successfully in folder", domain_name)
    except requests.exceptions.ConnectionError:
        print("Error: The website closed unexpectedly without providing a response. You can't retrieve any data from this website.")
