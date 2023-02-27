import requests
from rich import print as pprint

endpoint = 'http://127.0.0.1:8000/api/'

with requests.Session() as s:
    res = s.get(endpoint, json={'product_id':'123'})
    pprint(res.json())
