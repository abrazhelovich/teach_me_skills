# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from add_fields_to_db import add_rows

url = "https://pobe.atlassian.net/rest/api/3/field"

#url = "https://owp.atlassian.net/rest/api/3/field"

auth = HTTPBasicAuth("andreibandrei1506@gmail.com", "mTIFadgdYFPmbtf62beI1F1F")  #pobe project
#auth = HTTPBasicAuth("andrei_brazhalovich@epam.com", "xp74GdrD1zuWdbJU6kpc2964")  # owp

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
   key = i['key']
   name = i['name']
   #if i['key'] != 'statuscategorychangedate' or i['key'] != 'issuetype':
   #print(f'{key}  {name}')
   add_rows(key, name)

