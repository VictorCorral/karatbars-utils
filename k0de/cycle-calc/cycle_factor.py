#!/usr/bin/python


from argh import *

def plrc(l,r,c):
    print "Left {0} Right {1} Cycles {2}".format(l,r,c)

@arg('left',  type=int)
@arg('right', type=int)
def cycle_factor(left,right):
    cycles = 0
    while True:
        plrc(left, right, cycles)
        if ((right >= left) and left > 25 and right > 50):
            cycles += 1
            left -= 25
            right -= 50
        elif ((left >= right) and left > 50 and right > 25):
            cycles += 1
            right -= 25
            left -= 50
        else:
            print "All cycles done"
            break


dispatch_command(cycle_factor)
