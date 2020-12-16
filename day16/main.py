# Advent of Code day 16
import re
def inrange(lohi,num):
    return lohi[0] <= num <= lohi[1]
inputlist = []
with open('input.txt','r') as f:
    inputlist = f.readlines()
inputlist = [x.strip('\n') for x in inputlist]
#if all ints
#inputlist = [int(x) for x in inputlist]
getints = re.compile('\d+')
gettype = re.compile('(.*):')
lohis = []
lohidict = {}
for x in inputlist[0:20]:
    
    ints = getints.findall(x)
    numbertype = gettype.match(x)
    numbertype = numbertype[0]
    if ints:
        ints = [int(x) for x in ints]
        lohis.append((ints[0],ints[1]))
        lohis.append((ints[2],ints[3]))
        lohidict[numbertype] = [(ints[0],ints[1]),(ints[2],ints[3])]
nearby = []
for x in inputlist[25:]:
    nearby.append(x.split(','))
nearby = [int(item) for sublist in nearby for item in sublist]
invalidlist = []
for x in nearby:
    valid = 0
    for lohi in lohis:
        if inrange(lohi,x):
            valid += 1
    if valid == 0:
        invalidlist.append(x)
print("p1",sum(invalidlist))
myticket = [int(x) for x in inputlist[22].split(',')]
print(myticket)
ticketdict = {}
for x in invalidlist:
    nearby.remove(x)
for count, ticketnum in enumerate(nearby):
    for key,value in lohidict.items():
        for lohi in value:
            if inrange(lohi,ticketnum) and key not in ticketdict and count not in ticketdict.values():
                ticketdict[key] = count
print(ticketdict)