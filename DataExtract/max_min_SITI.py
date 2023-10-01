import requests
import csv
import os

site_address='https://ftp.itec.aau.at/datasets/video-complexity/2-SITI/all-frames/'
with open('../Crawl_result/list_of_video.txt', 'r') as file:
    for line in file:
        url = site_address+line.strip()[:-3]+ 'txt'  
        response = requests.get(url)
        if response.status_code == 200:
            with open(line +'csv', 'wb') as f:
                f.write(response.content)
            SI_col = 'SI'  
            TI_col = 'TI'

            max_value_SI = None
            min_value_SI = None
            max_value_TI = None
            min_value_TI = None
            if not os.path.exists('max_min_SITI.csv'):
                with open('max_min_SITI.csv', 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['name', 'max_SI', 'min_SI', 'max_TI', 'min_TI'])
            with open(line +'csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row[SI_col] != '':
                        value = float(row[SI_col])
                        if max_value_SI is None or value > max_value_SI:
                            max_value_SI = value
                        if min_value_SI is None or value < min_value_SI:
                            min_value_SI = value
                    if row[TI_col] != '':
                        value2 = float(row[TI_col])
                        if max_value_TI is None or value2 > max_value_TI:
                            max_value_TI = value2
                        if min_value_TI is None or value2 < min_value_TI:
                            min_value_TI = value2
            with open('max_min_SITI.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([line.strip()[:-4], max_value_SI , min_value_SI, max_value_TI, min_value_TI])
            os.remove(line +'csv')
        else:
            print('Failed to download the file.')