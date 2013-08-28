from treelib import *
from treelib.tree import DuplicatedNodeIdError
from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def i1(i):
    return iter(i)

def i2(i):
    return grouper(2, iter(i))

class ListToTree(object):

    def __init__(self, lis):
        self.pos = i1(lis)
        self.pos2= i2(lis[1:])
        self.tree = Tree()
        self.list_= lis
        self.build()

    def build(self):
        for e in self.pos:
            try:
                self.tree.create_node(e, e)
            except DuplicatedNodeIdError:
                pass
            self.append_children(e)

    def show(self):
        self.tree.show()

    def append_children(self, e):
        try:
            for child in self.pos2.next():
                self.tree.create_node(child, child, parent=e)
        except StopIteration:
            pass

