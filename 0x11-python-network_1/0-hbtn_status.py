#!/usr/bin/python3
"""A script that fetchess a url"""
import urllib.request


if __name__ == "__main__":
    url = Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
