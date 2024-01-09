#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
    using package requests"""


if __name__ == "__main__":

    import requests

    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    content = resp.text
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
