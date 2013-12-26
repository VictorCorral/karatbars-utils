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

# local
import user as userdata


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

    @try_method
    def find_bid_button(self):
        self.bid_button = self.browser.find_by_xpath('//a[@class="bid-button-link button-small"]')

    def item_price(self):
        price = self.browser.find_by_xpath('//*[@class="bid-price"]')
        return float(price.value[1::])


    @try_method
    def click_bid_button(self):
        self.bid_button.click()
        print "\tClicked."
        time.sleep(1)

    def login(self):
        print "Logging in..."
        self.browser.visit(url_for_action('login'))
        self.browser.fill('username', self.user['username'])
        self.browser.fill('password', self.user['password'])
        button = self.browser.find_by_id('btn_login')
        button.click()


    @try_method
    def execute_click(self):
        self.find_bid_button()
        self.click_bid_button()
        self.report_results()

    def report_results(self):
        self.bids_at_finish = self.bids_left()
        diff = self.bids_at_start - self.bids_at_finish
        bid_cost = diff * 0.50
        total_cost = bid_cost + self.item_price()
        print "\tBids used: {0}. Bid Cost at .50/bid = {1}. Total cost = {2}".format(diff, bid_cost, total_cost)

    def check_for_click(self):
        #self.countdown() <= 2 would be a neat test, but the DOM is
        # too freaky around this time to be playing games and you
        # have to get a click in at all costs.

        # it would be nice to not waste a click if someone else clicks
        # in the same few milliseconds but that is not possible
        # given the speed of DOM lookups, etc
        return True

    def chosen_auction(self):
        u = self.browser.url
        if re.search('\d+$', u):
            print "Chosen auction", u
            return u
        else:
            time.sleep(5)
            print "\tStill waiting for auction to be chosen"
            return self.chosen_auction()

    def wait_for_auction_choice(self):
        self.browser.visit(url_for_action('auctions'))
        return self.chosen_auction()



    def visit_binary(self):

        self.browser.visit(url_for_action('binary'))

        while True:
            sleep_time = self.sleep_time(10)
            print "\tSleeping for", sleep_time, "seconds"
            time.sleep(sleep_time)
            users = self.browser.find_by_css('.binary_text')
            for user in users:
                print user.text


    def sleep_time(self, s):
        if s <= 1:
            return 0
        elif s == 2:
            return 0
        elif s == 3 or s == 4:
            return 0.1
        else:
            return s - 4

    def bids_left(self):
        div = self.browser.find_by_xpath('//*[@class="bid-balance"]')
        #pdb.set_trace()
        return int(div.value)


    def countdown_div_value(self):
        countdown_div = self.browser.find_by_xpath(
            '//div[@class="timer countdown"]'
        )
        v = countdown_div.value.split(':')
        if "--" in v: # timer has not printed to screen
            return self.countdown_div_value()
        elif "Ended" in v:
            print "Auction ended."
            return None
        else:
            return v

    @try_method
    def countdown(self):
        c = self.countdown_div_value()
        if c is None:
            return None

        (h,m,s) = [int(v) for v in c]
        return h*60*60 + m*60 + s


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
