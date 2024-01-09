#!/usr/bin/python3
""" a Python script that takes in a URL,
    sends a request to the URL
    and displays the body of the response (decoded in utf-8).
    the code will also catch urllib.error.HTTPError
    and displays the error code"""


if __name__ == "__main__":
    from urllib import request
    from urllib import error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
