# https://curlconverter.com/

# terminal
cd Py
cd flaskapp
source ~/.virtualenvs/bensvenv3.10/bin/activate
echo $FLASK_APP
export FLASK_ENV=development
flask run

# browser
http://127.0.0.1:5000/countries

# python
response = requests.get("http://127.0.0.1:5000/countries")
response.json()
response.status_code
response.headers

# post from terminal
curl -i http://127.0.0.1:5000/countries \
-X POST \
-H 'Content-Type: application/json' \
-d '{"name":"Germany", "capital": "Berlin", "area": 357022}'

# post from python
# so darn useful https://curlconverter.com/
headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'name': 'Minnesota',
    'capital': 'StPaul',
    'area': 999,
}

response = requests.post('http://127.0.0.1:5000/countries', headers=headers, json=json_data)
response.json()

# get it again to see
response = requests.get("http://127.0.0.1:5000/countries")
response.json()
