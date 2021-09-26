import requests
import json
from main import selector
import token

headers = {
    "Authorization": "Bearer %s" % token,
}

payload = {
    "states": [
        {
        "selector": selector,
        "power": "on",
        }
    ],
}

response = requests.put('https://api.lifx.com/v1/lights/states', data=json.dumps(payload), headers=headers)

