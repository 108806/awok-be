import os, sys, json, requests
from rich import print as pprint

pprint(os.getcwd(), sys.version)



headers={
'Authorization':'Token 469d84428349870d9a1a60928291b240029f1d12',
'Content-Type': 'application/json; charset=UTF-8'
}

url = 'http://localhost:8000/get-user'

def get_user_by_id(id:int):

    data={ 'id' : '1' }
    with requests.Session() as S:
        params ={'id':'1'} #Case SENSITIVE!
        res = S.get(url, params=params, headers=headers)
        pprint('[*]', res.status_code, res.text)

if __name__ == '__main__':
    get_user_by_id(2)
