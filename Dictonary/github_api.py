import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"

response = requests.get(url)

complete_details = response.json()  # List

print(len(complete_details))
print(complete_details[0]["user"]["login"])

for element in range(len(complete_details)):
    print(complete_details[element]["user"]["login"])
