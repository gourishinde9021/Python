# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gourishinde9021.atlassian.net/rest/api/3/project"
API_TOKEN = "ATATT3xFfGF0GHkNOYO9K8jMsBamQv6-EapLfAY31KpSfik7xAmvQ4SuGxyN6uNK8z7UyWcg0tyWbrsXS82lLKyvFu5jfG8JKNknr4dakahhkDRVHFCuAqsgh9T1AL6hjjDg-pK0RCaBHd7sMP54pnNlDRvRCmuN8ZklwG0mXiIg9B5_TCUsooY=5CC161FF"
auth = HTTPBasicAuth("gourishinde9021@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)
name = output[0]["name"]
print(name)