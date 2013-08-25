#!/usr/bin/python


class Marketer:
    def __init__(self, kbid, url=None):
        self.kbid=kbid
        self.url=url

class Node:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

rows = [
    [ 'sbsmarketing' ],
    'kaelson amaboe'.split(),
    [ 'sweatgold', None, None, 'matosinho' ],
    [ 'herotti',   None, None, None, None, None, None, None ]
]

for row in rows:
    print row
