#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request to:
        http://0.0.0.0:5000/search_user with the letter as a parameter.

        - """

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    payload_tuples = []
    if (len(sys.argv) == 1):
        payload_tuples.append(("q", ""))
    else:
        payload_tuples.append(("q", sys.argv[1]))

    res = requests.post(url, data=payload_tuples)
    try:
        content = res.json()
    except requests.exceptions.JSONDecodeError():
        print("Not a valid JSON")
    else:
        if res.status_code == 204 or not content:
            print("No result")
        else:
            print("[{}] {}".format(content.get('id'), content.get('name')))
