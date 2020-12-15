import fileinput
from collections import Counter
from collections import defaultdict
from collections import deque
from functools import partial
import re

inputlist = []
for line in fileinput.input():
    inputlist.append(line.strip())

print(inputlist[0])
splitlist = inputlist[0].split(',')
splitlist = [int(x) for x in splitlist]
print(splitlist)


def p1(splitlist):
    num = 0
    # have to keep list of all nums and when they were said, perhaps dict
    mydeque = partial(deque, maxlen=2)
    numdict = defaultdict(mydeque)
    mylen = len(splitlist)
    for cnt in range(30000000):
        if cnt < mylen:
            num = splitlist[cnt]
        else:
            if num in numdict:
                if len(numdict[num]) == 1:
                    num = 0
                elif len(numdict[num]) > 1:
                    num = numdict[num][-1] - numdict[num][-2]
        numdict[num].append(cnt)
    return num


print("test 0,3,6:", p1([0, 3, 6]))
# import timeit
# print(timeit.timeit(lambda: p1([0,3,6]),number = 1))
print("p1: ", p1(splitlist))
