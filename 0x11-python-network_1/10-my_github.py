#!/usr/bin/python3
""" a Python script that takes the user's GitHub credentials
    (username and password) and uses the GitHub API to display the id """

if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth
    username = sys.argv[1]
    password = sys.argv[2]

    headers = HTTPBasicAuth(username, password)
    resp = requests.get("https://api.github.com/user", auth=headers)
    print(resp.json().get('id'))
