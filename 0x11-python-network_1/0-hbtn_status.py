#!/usr/bin/python3
'''Script that fetches https://alx-intranet.hbtn.io/status.
'''
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        s = 'Body response:\n'
        s += '\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(
                type(html), html, html.decode('utf8'))
        print(s)
