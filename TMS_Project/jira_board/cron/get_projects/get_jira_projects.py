import requests
from requests.auth import HTTPBasicAuth
import json
from add_rows_to_db import add_rows

url = "https://pobe.atlassian.net/rest/api/3/project/"

auth = HTTPBasicAuth()  

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

decode = response.content.decode('UTF-8')
result = json.loads(decode)

for i in result:
   number = i['id']
   key = i['key']
   name = i['name']
   add_rows(number, key, name)
   
