#!/usr/bin/python3
"""  POST an email #1 """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {"email": email}
    res = requests.post(url, data = param)
    print(res.text)

