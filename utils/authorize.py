import requests
import os
import json
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_token():

    URL_AUTH = os.getenv('URL_AUTH')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    AUDIENCE = os.getenv('AUDIENCE')

    payload_dict = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "audience": AUDIENCE,
    "grant_type": "client_credentials"
    } 
    payload = json.dumps(payload_dict)

    headers = { 'content-type': "application/json" }

    response = requests.post(URL_AUTH,data=payload,headers=headers)
    res = json.loads(response)
    print(res)
    data = res["access_token"]

    return data