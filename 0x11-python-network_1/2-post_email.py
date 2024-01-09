#!/usr/bin/python3
""" a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    import sys

    value = {"email": sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode("utf-8")
    req_obj = request.Request(sys.argv[1], data)
    with request.urlopen(req_obj) as response:
        print(response.read().decode("utf-8"))
