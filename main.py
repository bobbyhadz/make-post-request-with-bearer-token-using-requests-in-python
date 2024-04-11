# Python requests: Making an HTTP request with a Bearer Token

import requests

url = 'https://jsonplaceholder.typicode.com/users'

data = {'id': 1, 'name': 'bobby hadz'}

headers = {
    'Authorization': 'Bearer YOUR_JWT_TOKEN',
}

response = requests.post(
    url,
    data=data,
    headers=headers,
    timeout=30
)

print(response.status_code)  # 👉️ 201

result = response.json()
print(result)  # 👉️ {'id': 11, 'name': 'bobby hadz'}
