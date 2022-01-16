import requests
import pprint
import pandas as pd
import config

url = config.endpoint

headers = config.headers
r = requests.request("GET", url, headers=headers)

output = 'list.csv'
message_data = []

pprint.pprint(r.text)
print(r.status_code)