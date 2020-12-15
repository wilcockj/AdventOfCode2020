import fileinput
from collections import Counter
import re

inputlist = []
for line in fileinput.input():
    inputlist.append(line.strip())


completedinstructions = []
totest = []
for i, x in enumerate(inputlist):
    if x.split()[0] == 'jmp' or x.split()[0] == 'nop':
        totest.append(i)
print(totest)
op = 0
acc = 0
# change random jmp to nop or nop to jmp
# keep testing until terminates normally i.e. op == len(inputlist)-1
testnum = 0
while True:

    if op in completedinstructions or op > len(inputlist) - 1:
        completedinstructions = []
        op = 0
        testnum += 1
    if inputlist[op] == '':
        break
    instruction, increase = inputlist[op].split()
    increase = [increase[0], increase[1:]]

    print(testnum)
    if op == totest[testnum]:
        if instruction == 'jmp':
            instruction = 'nop'
        elif instruction == 'nop':
            instruction = 'jmp'
    completedinstructions.append(op)

    if instruction == 'acc':
        if increase[0] == '+':
            num = increase[1]
            acc += int(num)
        elif increase[0] == '-':
            num = increase[1]
            acc -= int(num)
        op += 1
    elif instruction == 'jmp':
        if increase[0] == '+':
            num = increase[1]
            op += int(num)
        elif increase[0] == '-':
            num = increase[1]
            op -= int(num)
    elif instruction == 'nop':
        op += 1
print(acc)
