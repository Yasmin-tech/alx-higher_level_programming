#!/usr/bin/python3
""" This model contains the code to fetches
    https://alx-intranet.hbtn.io/status
    and print the type, content type and if if it is a utf encoded
"""

if __name__ == "__main__":
    from urllib import request

    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        print("Body response:")
        content = response.read()
        print(" - type:", type(content))
        print(" - content:", content)
        print(" - utf8 content:", content.decode("utf-8"))
