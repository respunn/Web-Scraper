import requests
from bs4 import BeautifulSoup
import os
import shutil
from urllib.parse import urlparse, urljoin

# get the directory of the script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# keep prompting user for website URL until they type "exit"
while True:
    url = input("Enter the URL of the website you want to download (or 'exit' to quit): ")

    if url == "exit":
        break

    try:
        # send a GET request to the URL and get the response
        response = requests.get(url)

        # parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # extract domain name from URL and create a directory with that name to store the HTML and CSS files
        domain_name = urlparse(url).netloc
        output_folder = os.path.join(script_dir, 'output', domain_name)

        # delete the old folder if it exists
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)

        # create a new folder
        os.makedirs(output_folder)

        # create a directory to store the images
        images_folder = os.path.join(output_folder, 'images')
        os.makedirs(images_folder, exist_ok=True)

        # save the HTML code to a file
        html_content = str(soup)
        with open(os.path.join(output_folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)

        # save the images to files
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                # join the base URL of the website with the relative URL of the image
                img_url = urljoin(url, src)
                img_content = requests.get(img_url).content
                filename = os.path.join(images_folder, src.split('/')[-1])
                with open(filename, 'wb') as f:
                    f.write(img_content)

        # print a success message after saving the files
        print("HTML, CSS, and images saved successfully in folder", domain_name)
    except requests.exceptions.ConnectionError:
        # print an error message if the website is not responding
        print("Error: The website closed unexpectedly without providing a response. You can't retrieve any data from this website.")
