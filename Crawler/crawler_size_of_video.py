import requests
from bs4 import BeautifulSoup

# Define the URL of the web page you want to crawl
url = 'https://ftp.itec.aau.at/datasets/video-complexity/1-ref/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <td> elements containing numeric values
    numeric_td_elements = []
    
    for td in soup.find_all('td'):
        # Check if the content of the <td> is a numeric value
        try:
            if td.get("align") == "right":
                if 'M' in td.text:
                    value = str(float(td.text.strip('M')) * 1024)
                    numeric_td_elements.append(value)
                if  'K' in td.text:
                    value = value.strip('K')
                    numeric_td_elements.append(value)
        except ValueError:
            pass
    
    with open('../Crawl_result/size_of_video.txt', 'w') as file:
        file.write('size\n')
        for value in numeric_td_elements:
            file.write(str(value) + '\n')
    
    print("Numeric values have been written to 'size_of_video.txt'.")
else:
    print("Failed to retrieve the web page. Status code: response.status_code",response.status_code)