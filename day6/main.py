import fileinput
import re


def inrange(s, l, h):
    return l <= int(s) <= h


d = []
for x in fileinput.input():
    d.append(x.strip())
s = ""
l = []
l.append([])
counter = 0
for x in range(len(d)):
    if d[x] != '':
        l[counter].append(d[x])
    else:
        l.append([])
        counter += 1
setlist = []
for x in l:
    s = ''
    for y in x:
        s += ''.join(set(y))
    setlist.append(len(''.join(set(s))))
print(sum(setlist))
uniquecount = 0
for y, x in enumerate(l):
    s = ''
    '''
    for y in range(len(x) - 1):
        if y == 0:
            s = ''.join(set(x[y]).intersection(x[y + 1]))
        else:
            s = ''.join(set(s).intersection(x[y + 1]))
        print(s)
    '''

    s = x[0]
    for y in x:
        s = set(s).intersection(y)
    s = ''.join(s)
    # print(x)
    # print(s)
    uniquecount += len(s)
print(uniquecount)
