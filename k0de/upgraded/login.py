#!/usr/bin/python

# system
from collections import defaultdict
from functools import wraps
import pdb
import pprint
import re
import sys
import time
import traceback

# pypi
from splinter import Browser
from treelib import Tree

# local
import user as userdata
import list_to_tree


pp = pprint.PrettyPrinter(indent=4)

base_url = 'http://www.karatbars.com'
action_path = dict(
    login = "index.php?page=login_1",
    binary = "members.php?page=binarytree"
)

def url_for_action(action):
    return "{0}/{1}".format(base_url,action_path[action])

def try_method(fn):
    @wraps(fn)
    def wrapper(self):
        try:
            return fn(self)
        except:
            print traceback.format_exc()
            self.visit_auction()

    return wrapper


class Entry(object):

    def __init__(self, user, browser):
        self.user=user
        self.browser=browser

    def login(self):
        print "Logging in..."
        self.browser.visit(url_for_action('login'))
        self.browser.fill('username', self.user['username'])
        self.browser.fill('password', self.user['password'])
        button = self.browser.find_by_id('btn_login')
        button.click()

    def visit_binary(self):
        self.browser.visit(url_for_action('binary'))

        tree = Tree()

        while True:
            users = self.browser.find_by_css('.binary_text')
            users = [u.text for u in users]
            l = list_to_tree.ListToTree(users)
            l.show()

            sleep_time = 5
            print "\tSleeping for", sleep_time, "seconds"
            time.sleep(sleep_time)


def main():
    with Browser() as browser:

        for user in userdata.users:
            e = Entry(user, browser)
            e.login()
            e.visit_binary()
            while True: pass

if __name__ == '__main__':

    if len(sys.argv) == 2:
        bid_url = sys.argv[1]
    else:
        bid_url = None
    main(bid_url)
