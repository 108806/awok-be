import os, sys, json, requests
from rich import print as pprint

pprint(os.getcwd(), sys.version)

data = {
    "username": "john_snow",
    "password": "Northling123",
}

headers = {'Content-Type': 'application/json; charset=UTF-8'}

url = 'http://localhost:8000/api/token'

with requests.Session() as S:
    JSONdata = json.dumps(data, indent=4)
    pprint('[*]', JSONdata)
    res = S.post(url, data=JSONdata, headers=headers)
    pprint('[*]', res.status_code, res.text)
