# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import codecs
import sys

import mmh3
import requests
from sys import argv

def cal_hash(path):
    response = requests.get(path)
    ct = response.content
    favicon = codecs.encode(ct,encoding='base64')
    hash = mmh3.hash(favicon)
    print(hash)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = "http://142.4.98.122/view/img/favicon.ico"
    p = sys.argv
    if len(p)==2:
        cal_hash(p[1])
    else:
        print("Please input the url")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
