# Advent of Code day 16
import re
inputlist = []
with open('input.txt','r') as f:
    inputlist = f.readlines()
inputlist = [x.strip('\n') for x in inputlist]
#if all ints
#inputlist = [int(x) for x in inputlist]
getints = re.compile('\d+')
gettype = re.compile('(.*):')
lohis = []
for x in inputlist[0:20]:
    
    ints = getints.findall(x)
    numbertype = gettype.match(x)
    if ints:
        ints = [int(x) for x in ints]
        lohis.append((ints[0],ints[1]))
        lohis.append((ints[2],ints[3]))
for x in inputlist[25:]:
    print(x)