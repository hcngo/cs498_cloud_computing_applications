import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1':  '34.215.12.31:80',
		'ip_address2':  '54.201.242.61:80',
		'load_balancer' :  'Mp1ALB-1220530125.us-west-2.elb.amazonaws.com',
		'submitterEmail':  'hieua0609ptnk+coursera@gmail.com',
		'secret':  'Vthf44PUaOav3RLq'
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)