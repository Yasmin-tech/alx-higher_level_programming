#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable found in the
    header of the response using requests package"""


if __name__ == "__main__":
    import requests
    import sys

    resp = requests.get(sys.argv[1])
    print(resp.headers['X-Request-Id'])
