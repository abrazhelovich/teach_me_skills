import requests
from requests.auth import HTTPBasicAuth
import json
from jira_board.cron.get_jira_users.add_user_to_db import add_rows

url = "https://pobe.atlassian.net/rest/api/3/users/search"

auth = HTTPBasicAuth("", "")

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
   if i['accountType'] != 'app':
      key = i['accountId']
      name = i['displayName']
      add_rows(key, name)