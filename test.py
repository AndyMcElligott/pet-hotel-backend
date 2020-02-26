import requests, json

loginInfo = {'username': 'Luke', 'password': 'l'}

loginInfoJson = json.dumps(loginInfo)
x = requests.Session()
# http://localhost:5000/api/user/logout
print(x.post('http://localhost:5000/api/user/login', loginInfoJson, headers={'Content-Type': 'application/json'}  ))
# x = requests.post('http://localhost:5000/api/user/logout')
result = x.get('http://localhost:5000/api/user/')

print(x.cookies)
