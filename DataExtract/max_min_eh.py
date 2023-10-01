import requests
import csv
import os

site_address='https://ftp.itec.aau.at/datasets/video-complexity/3-Eh/all-frames/' #'https://ftp.itec.aau.at/datasets/video-complexity/2-SITI/all-frames/'
with open('../Crawl_result/list_of_video.txt', 'r') as file:
    for line in file:
        url = site_address+line.strip()[:-3]+ 'txt'  
        response = requests.get(url)
        if response.status_code == 200:
            with open(line +'csv', 'wb') as f:
                f.write(response.content)
            E_col = ' E'  
            h_col = ' h'

            max_value_E = None
            min_value_E = None
            max_value_h = None
            min_value_h = None
            if not os.path.exists('max_min_Eh.csv'):
                with open('max_min_Eh.csv', 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow(['name', 'max_E', 'min_E', 'max_h', 'min_h'])
            with open(line +'csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row[E_col] != '':
                        value = float(row[E_col])
                        if max_value_E is None or value > max_value_E:
                            max_value_E = value
                        if min_value_E is None or value < min_value_E:
                            min_value_E = value
                    if row[h_col] != '':
                        value2 = float(row[h_col])
                        if max_value_h is None or value2 > max_value_h:
                            max_value_h = value2
                        if min_value_h is None or value2 < min_value_h:
                            min_value_h = value2
            with open('max_min_Eh.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([line.strip()[:-4], max_value_E , min_value_E, max_value_h, min_value_h])
            os.remove(line +'csv')
        else:
            print('Failed to download the file.')