from treelib import *
from treelib.tree import DuplicatedNodeIdError
from itertools import izip_longest

tree = Tree()
nums = range(1,9)

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def i1(i):
    return iter(i)

def i2(i):
    return grouper(2, iter(i))

pos=i1(nums)
pos2=i2(nums[1:])

def append_children(e):
    try:
        for child in pos2.next():
            tree.create_node(child, child, parent=e)
    except StopIteration:
        pass

for e in pos:
    try:
        tree.create_node(e, e)
    except DuplicatedNodeIdError:
        pass
    append_children(e)

tree.show()
