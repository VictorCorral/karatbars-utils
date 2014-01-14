o = open('current.txt')
a = open('all.txt')

oset = set()
aset = set()

for line in o.read().splitlines():
    if not len(line): continue
    line.rstrip('\r\n')
    oset.add(line.lower())

print "Number of countries current in = {0}. Countries = {1}.".format(
    len(oset), sorted(list(oset)))

for line in a.read().splitlines():
    if not len(line): continue
    line = line.lower()
    line.rstrip('\r\n')
    aset.add(line.lower())

print "Number of countries total = {0}. Countries = {1}.".format(
    len(aset), sorted(list(aset)))

d = aset - oset
print "number of countries to open = {0}. Countries={1}".format(
    len(d), "\n".join(sorted(list(d))))
