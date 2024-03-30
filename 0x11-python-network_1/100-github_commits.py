#!/usr/bin/python3
"""lists the 10 most recent commits on a public GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":

    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)
    commits = response.json()

    # print(commits)

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
