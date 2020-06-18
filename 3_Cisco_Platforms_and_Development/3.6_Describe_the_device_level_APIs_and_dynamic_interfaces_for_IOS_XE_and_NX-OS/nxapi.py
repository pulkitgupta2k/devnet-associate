import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/ins"
user = "admin"
password = "Admin_1234!"
headers = {'content-type': 'application/json'}

payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "sh ip int brief",
        "output_format": "json"
    }
}

response = requests.post(
    url,
    data=json.dumps(payload),
    headers=headers,
    auth=(user, password),
    verify=False
).json()

pprint(response)