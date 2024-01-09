#!/usr/bin/python3
""" a Python script that takes in a URL,
    sends a request to the URL
    and displays the body of the response.
    if the status code of the response is 400 or greater, will print it"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    resp = requests.get(url)
    if (resp.status_code >= 400):
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
