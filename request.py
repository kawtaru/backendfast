import requests
import json

url = 'https://tame-jade-buffalo-kilt.cyclic.app/:3000/check'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}
data = {
    "text": "Ayah"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

