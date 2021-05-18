import requests
from requests.auth import HTTPBasicAuth
import json
from add_rows_to_db import add_rows

url = "https://pobe.atlassian.net/rest/api/3/project/"

auth = HTTPBasicAuth("andreibandrei1506@gmail.com", "mTIFadgdYFPmbtf62beI1F1F")  #pobe project

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

decode = response.content.decode('UTF-8')
result = json.loads(decode)

for i in result:
   number = i['id']
   key = i['key']
   name = i['name']
   add_rows(number, key, name)
   #print(f'{key}  {name}')
