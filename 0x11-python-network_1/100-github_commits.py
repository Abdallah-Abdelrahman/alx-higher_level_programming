#!/usr/bin/python3
'''List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
'''
import sys
from requests import get, exceptions


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    try:
        req = get(url, params={'per_page': 10})
        commits = req.json()
        for cmt in commits:
            print('{}: {}'.format(cmt['sha'],
                                  cmt['commit']['author']['name']))
    except exceptions.HTTPError:
        pass
