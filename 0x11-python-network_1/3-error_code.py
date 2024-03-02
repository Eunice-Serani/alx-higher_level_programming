#!/usr/bin/python3
"""
This implements a script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.error
    
    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
