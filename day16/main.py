# Advent of Code day 16
import re
from collections import defaultdict
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
    numbertype = numbertype[1]
    if ints:
        ints = [int(x) for x in ints]
        lohis.append((ints[0],ints[1]))
        lohis.append((ints[2],ints[3]))
        lohidict[numbertype] = [(ints[0],ints[1]),(ints[2],ints[3])]
nearby = []
for x in inputlist[25:]:
    nearby.append([int(item) for item in x.split(',')])
validlist = []
error_rate = 0
for ticket in nearby:
    for num in ticket:
        valid = 0
        for lohi in lohis:
            if inrange(lohi,num):
                valid += 1
                break
        if valid == 0:
            error_rate += num
            break
    if valid >= 1 :
        validlist.append(ticket)    
print("p1",error_rate)
myticket = [int(x) for x in inputlist[22].split(',')]
#possibledict = defaultdict(lambda: lohidict.keys())
possibledict = {i: set(lohidict.keys()) for i in range(len(validlist[0]))}
for ticket in validlist:
    for count,num in enumerate(ticket):
        for key,value in lohidict.items():
            possible = False
            for lohi in value:
                if inrange(lohi,num):
                    possible = True
                    break
            if not possible:
                possibledict[count].discard(key)

for i in possibledict.values():
    for key,value in possibledict.items():
        if len(value) == 1:
            for x in possibledict.keys():
                #print(str(list(value)[0]))
                singlevalue = str(list(value)[0])
                if x != key and singlevalue in possibledict[x]:
                    possibledict[x].remove(singlevalue)
                    print(f"removed {singlevalue} from index {x}")
#print(possibledict)
ans = 1
for key in possibledict:
    if str(list(possibledict[key])[0]).startswith("departure"):
        ans *= myticket[key]
'''
print(myticket)
ticketdict = defaultdict(list)
for x in invalidlist:
    nearby.remove(x)
for count, ticketnum in enumerate(nearby):
    possible = 0
    for key,value in lohidict.items():
        for lohi in value:
            if inrange(lohi,ticketnum):
                ticketdict[key].append(count)         
for key,value in ticketdict.items():
    print(len(value))
    #print(key,value)
'''