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
        pprint('[*] search by id:', res.status_code, res.text)
        return res.status_code
    
def get_user_by_uname(uname:str):
    data={ 'username' : uname }
    with requests.Session() as S:
        params ={'id':'1'} #Case SENSITIVE!
        res = S.get(url, params=params, headers=headers)
        pprint('[*] search by username: ', res.status_code, res.text)
        return res.status_code

def get_user_by_email(string:str):
    with requests.Session() as S:
        #Case SENSITIVE!
        params ={"email": string}
        res = S.get(url, params=params, headers=headers)
        pprint('[*] search by email: ', res.status_code, res.text)
        return res.status_code

if __name__ == '__main__':
    assert get_user_by_id(2) == 200, 'get user by id error'
    assert get_user_by_uname('john_snow') == 200, 'get user by uname error'
    assert get_user_by_email('ido@ntk.now') == 200, 'get user by email error'
    print('DONE.')
