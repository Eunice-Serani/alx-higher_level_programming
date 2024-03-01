#!/usr/bin/python3
"""This implements a script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
