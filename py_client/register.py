import requests 
import os, sys, json
from rich import print as pprint

pprint(os.getcwd(), sys.version)

data = {
    "username": "john_snow",
    "first_name": "john",
    "last_name": "snow",
    "email": "ido@ntk.now",
    "password": "Northling123",
    "password2": "Northling123",
}

headers = {'Content-Type': 'application/json; charset=UTF-8'}

url = 'http://localhost:8000/register'

with requests.Session() as S:
    JSONdata = json.dumps(data, indent=4)
    pprint('[*]', JSONdata)
    res = S.post(url, data=JSONdata, headers=headers)
    pprint('[*]', res.status_code, res.text)

