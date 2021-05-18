import requests
from requests.auth import HTTPBasicAuth
import json
from add_fields_to_db import add_rows

url = "https://pobe.atlassian.net/rest/api/3/field"

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
   key = i['key']
   name = i['name']
   add_rows(key, name)

