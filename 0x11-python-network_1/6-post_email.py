#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response using requests model"""


if __name__ == "__main__":
    import requests
    import sys

    data = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data=data)
    print(resp.text)
