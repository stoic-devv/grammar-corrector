from HTMLParser import HTMLParser
import numpy as np
import pandas as pd


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def htmlstripper(text):
    return strip_tags(text)

def store_data(str):
    df = pd.read_csv(str)
    data = df.DESCRIPTION
    pid = df.PRODUCT_ID
    data = data.apply(htmlstripper)
    return pid, data