import requests as requests
import json as json

r = requests.get('http://52.64.2.128:5000/api/v1/projects')
data = r.json();
assert ('flask' in data['projects'])

r = requests.post('http://52.64.2.128:5000/api/v1/start', json={"id" : "flask"})

r = requests.get('http://52.64.2.128:5001/')
assert(r.text.find("Hello World") == 0);

r = requests.post('http://52.64.2.128:5000/api/v1/stop', json={"id" : "flask"})

success = False
try:
    r = requests.get('http://52.64.2.128:5001/')
except:
    success = True

assert(success)
