import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to crawl
url = 'https://ftp.itec.aau.at/datasets/video-complexity/1-ref/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the elements containing the custom values you want to extract
    custom_elements = soup.find_all('a')  # Replace with appropriate HTML tags and attributes

    # Define the file where you want to write the extracted values
    output_file = 'list_of_video.txt'

    # Open the file in write mode
    with open(output_file, 'w') as file:
        # Loop through the extracted elements and write custom values to the file, one per line
        for element in custom_elements:
            custom_value = element.text.strip()  # Extract the text of the element
            file.write(custom_value + '\n')

    print(f'Custom values extracted and saved to {output_file}')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')
