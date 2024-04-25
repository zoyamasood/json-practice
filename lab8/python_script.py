import json
import requests 

data_file = '/workspace/json-practice/lab8/schacon.repos.json'
output_file = '/workspace/json-practice/lab8/chacon.csv'

with open(data_file, 'r') as file:
    data = json.load(file)

with open(output_file, 'a') as file: 
    for entry in data[0:5]: 
        name = entry['name']
        html_url = entry['html_url']
        updated_at = entry['updated_at']
        visibility = entry['visibility']

        file.write(name + ',' + html_url + ',' + updated_at + ',' + visibility + '\n')

    



