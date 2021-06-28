import requests
import json

url = "http://ec2-35-172-216-189.compute-1.amazonaws.com:30000/api/v1/targets?state=active"
r = requests.get(url)
print(r.json())
data = r.json()
print(data)

for x in data['data']['activeTargets']:
    try:
        print(x['discoveredLabels']['__meta_kubernetes_pod_name'])
    except KeyError:
        print('[ERROR] Key not available')

