import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1':  '34.215.12.31:5000',
		'ip_address2':  '54.201.242.61:5000',
		'load_balancer' :  'SecondALB-1024867037.us-west-2.elb.amazonaws.com',
		'submitterEmail':  'hieua0609ptnk+coursera@gmail.com',
		'secret':  'IoZX5zTYhBC8wwef'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)