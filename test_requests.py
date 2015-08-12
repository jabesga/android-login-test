import requests

#headers = {}
#headers = {'Authorization': 'Token 4070bfa4f47854f3fe7f466a7a01743f105726be'}
#r = requests.get('http://localhost:8000/router/users/', headers=headers)

r = requests.post('http://localhost:8000/api-token-auth/', data={'username':'admin', 'password':'admin'})
print(r.text)