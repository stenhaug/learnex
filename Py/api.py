# see flaskapp

# https://nordicapis.com/the-bezos-api-mandate-amazons-manifesto-for-externalization/
# https://realpython.com/api-integration-in-python/

import requests

# GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()
response.status_code
response.headers

# POST
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()
response.status_code

# PUT
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
response.json()
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()
response.status_code
