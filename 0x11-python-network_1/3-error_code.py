#!/usr/bin/python3
'''script that takes in a URL and an email, sends a POST request,
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        res = urlopen(req)
        print(res.read().decode('utf8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
