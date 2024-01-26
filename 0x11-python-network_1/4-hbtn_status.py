#!/usr/bin/python3
""" 4-hbtn_status.py """
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)
status_code = response.status_code

if status_code == 200:
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text.replace('\n', '\n\t\t')))
else:
    print("Error: Unable to fetch the URL. Status code:", status_code)

