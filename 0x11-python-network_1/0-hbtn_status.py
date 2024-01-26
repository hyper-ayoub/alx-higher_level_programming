#!/usr/bin/python3
""" Write a Python script that fetches https://alx-intranet.hbtn.io/status """

import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
