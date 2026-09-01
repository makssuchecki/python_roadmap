import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)

r.headers["content-type"]
# application/json; charset=utf8

r.encoding
# utf-8

r.text
# {"type": "User"...

r.json()
# {'private_gists": 419, ...

r.encoding 
r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)