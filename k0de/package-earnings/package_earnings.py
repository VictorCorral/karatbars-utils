earnings=dict(
    bronze=10,
    silver=40,
    gold=60,
    vip=80)

cost=dict(
    bronze=130,
    silver=300,
    gold=750,
    vip=2000)

profit = { pkg : -c for pkg,c in cost.iteritems() }

ordering = 'bronze silver gold vip'.split()

for i in xrange(30):
    print ",".join([ str(profit[i]) for i in ordering ])

    for pkg in earnings:
        profit[pkg] += earnings[pkg]
