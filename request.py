import requests
import json

url = 'https://tame-jade-buffalo-kilt.cyclic.app/check'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "text": "Ayah"
}

response = requests.post(url, headers=headers, json=data)


print(response.json())
if response.status_code == 200:
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
