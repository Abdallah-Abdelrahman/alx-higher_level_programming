#!/usr/bin/python3
'''Script that fetches https://alx-intranet.hbtn.io/status.

- You must use the package urllib
- You are not allowed to import any packages other than urllib
- You must use a with statement
'''
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:\n\t- type: {}\
              \n\t- content: {}\n\t- utf8 content: {}'
              .format(type(html), html, html.decode('utf8')))
