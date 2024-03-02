#!/usr/bin/python3
'''script that takes in a letter and sends a POST request to,
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import sys
from requests import get, exceptions


if __name__ == '__main__':
    q = sys.argv[2] if len(sys.argv) > 2 else ""
    url = 'http://0.0.0.0:5000/search_user'
    try:
        req = get(url, params={'q': q})
        req.raise_for_status()
        json = req.json()
        print('No result' if len(json) == 0 else '[{}] {}'
              .format(json['id'], json['name']))
    except exceptions.JSONDecodeError:
        print('Not a valid JSON')
    except exceptions.HTTPError:
        pass
