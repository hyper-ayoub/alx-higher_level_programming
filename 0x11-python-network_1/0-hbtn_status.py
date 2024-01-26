#!/usr/bin/python3
"""0x11. Python - Network #1, task 0. What's my status? #0
"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf-8')))
    # charset can be gained with response.headers.get_content_charset()
