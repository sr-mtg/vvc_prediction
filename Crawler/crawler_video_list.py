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
    output_file = '../Crawl_result/list_of_video.txt'

    # Open the file in write mode
    with open(output_file, 'w') as file:
        # Loop through the extracted elements and write custom values to the file, one per line
        for element in custom_elements:
            custom_value = element.text.strip()  # Extract the text of the element
            file.write(custom_value + '\n')
    
    with open(output_file, 'r') as input_file:
        # Read all lines from the input file
        lines = input_file.readlines()

    # Check if the file has at least five lines
    if len(lines) >= 5:
        # Remove the first five lines
        lines = lines[5:]

        # Open the output file in write mode
        with open(output_file, 'w') as output_file:
            # Write the remaining lines to the output file
            output_file.writelines(lines)

    print(f'Custom values extracted and saved to {output_file}')
else:
    print(f'Failed to retrieve the web page. Status code: {response.status_code}')

