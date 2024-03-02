#!/usr/bin/python3
'''script that takes in a URL,
sends a request to the URL and displays the body of the response.
'''
import sys
from requests import get, exceptions


if __name__ == '__main__':
    try:
        req = get(sys.argv[1])
        req.raise_for_status()
        print(req.text)
    except exceptions.HTTPError:
        if req.status_code >= 400:
            print('Error code: {}'.format(req.status_code))
