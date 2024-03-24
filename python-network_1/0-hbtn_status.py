#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request
if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    if url.startsWith("https://"):
        url = 'https://alu-intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
