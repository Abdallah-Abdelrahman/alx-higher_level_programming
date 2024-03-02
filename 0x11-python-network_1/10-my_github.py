#!/usr/bin/python3
''' script that takes your GitHub credentials (username and password),
and uses the GitHub API to display your id
'''
import sys
from requests import get, exceptions


if __name__ == '__main__':
    token = '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'
    _, user, psw = sys.argv
    url = f'https://api.github.com/users/{user}'
    header = {
            "Authorization": f"Bearer {psw}",
            'Accept': 'application/vnd.github+json',
    }

    try:
        req = get(url, headers=header)
        req.raise_for_status()
        json = req.json()
        print(json['id'])
    except exceptions.HTTPError as e:
        print(None)
