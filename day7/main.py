import fileinput
from collections import Counter
import re

inputlist = []
for line in fileinput.input():
    inputlist.append(line.strip())
baglist = []
canholdgold = {}
bagdict = {}
testbagdict = {}
parents = []
bagnumberdict = {}
# make dicitionary write if a bag can contain shiny gold
# then look through and see if a bag contains any of these bags


def recursivebagcheck(bags, target, parents):
    for outer, inner in bags.items():
        if target in inner and outer not in parents:
            parents.append(outer)
            recursivebagcheck(bags, outer, parents)

    return len(parents)


def recursivebagcount(bags, parents):
    total = 1
    for child, number in bags[parents].items():
        total += int(number) * recursivebagcount(bags, child)
    return total


def p1(inputlist):
    # make dictionary
    for x in range(10):
        for rule in inputlist:
            innerbags = []
            parent, children = re.match(r'(.+?)s? contain (.+)', rule).groups()
            children = re.findall(r'(\d) ([ a-z]+bag)?', children)

            '''
            outerbag = rule.split("bags")[0].strip()
            baglist.append(outerbag)
            innerbags = []
            if rule.split("contain")[1].strip() == "no other bags.":
                # print(rule)
                canholdgold[outerbag] = 0
            elif Counter(rule)[","] > 0:
                innerbags = rule.split("contain")[1].split(",")
                innerbags = [re.sub('\d', '', bag) for bag in innerbags]
                innerbags = [re.sub('bag.|bags.|contain', '', bag)
                             for bag in innerbags]
                innerbags = [x.strip() for x in innerbags]
                innerbags = [x.rstrip(" .") for x in innerbags]
            else:
                innerbags = rule.split("contain")[1]
                innerbags = re.sub('\d|bags.|bag.', '', innerbags)
                innerbags = innerbags.strip()
                innerbags = [innerbags]
            # print(outerbag,innerbags)
            bagdict[outerbag] = innerbags
            '''
            # print(parent)
            # print(children)
            for x in children:
                innerbags.append(x[1])
            if "shiny gold bag" in innerbags:
                canholdgold[parent] = 1
            for x in innerbags:
                if x in canholdgold:
                    if canholdgold[x] == 1:
                        canholdgold[parent] = 1

            if parent not in bagdict:
                bagdict[parent] = []

            for number, bag in children:
                bagdict[parent].append(bag)

            if parent not in bagnumberdict:
                bagnumberdict[parent] = {}

            for number, bag in children:
                bagnumberdict[parent][bag] = number

            # print(innerbags)
            # print(len(canholdgold))
            # print(len(canholdgold))
            goldholdcount = 0
            for x in canholdgold.values():
                if x == 1:
                    goldholdcount += 1
    goldholdcount = 0
    for x in canholdgold.values():
        if x == 1:
            goldholdcount += 1
    print(goldholdcount)
    parents = []

    print(recursivebagcheck(bagdict, "shiny gold bag", parents))
    parents = {}
    print(recursivebagcount(bagnumberdict, "shiny gold bag") - 1)


p1(inputlist)
# print(set(baglist))
