from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# create a flask application instance
app = Flask(__name__)

@app.route("/createJIRA", methods = ['POST'])            # Decorator
def createJIRA():
    url = "https://gourishinde9021.atlassian.net/rest/api/3/project"
    API_TOKEN = "ATATT3xFfGF0GHkNOYO9K8jMsBamQv6-EapLfAY31KpSfik7xAmvQ4SuGxyN6uNK8z7UyWcg0tyWbrsXS82lLKyvFu5jfG8JKNknr4dakahhkDRVHFCuAqsgh9T1AL6hjjDg-pK0RCaBHd7sMP54pnNlDRvRCmuN8ZklwG0mXiIg9B5_TCUsooY=5CC161FF"
    auth = HTTPBasicAuth("gourishinde9021@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first Jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        
        "issuetype": {
        "id": "10005"
        },
        
        "project": {
        "key": "PYT"
        },
        
        "summary": "First jira",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0')