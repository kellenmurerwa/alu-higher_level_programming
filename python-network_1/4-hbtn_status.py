#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    if url.startswith("https://"):
        url = "https://alu-intranet.hbtn.io/status"
    r = requests.get(url)
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
