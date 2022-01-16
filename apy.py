import requests
import pprint
import pandas as pd
import config

url = config.endpoint

headers = config.headers
r = requests.request("GET", url, headers=headers)

pprint.pprint(r.text)
print(r.status_code)