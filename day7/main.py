import fileinput
from collections import Counter
import re

inputlist = []
for line in fileinput.input():
    inputlist.append(line.strip())
baglist = []
canholdgold = {}
# make dicitionary write if a bag can contain shiny gold
# then look through and see if a bag contains any of these bags


def p1(inputlist):
    # make dictionary

    for x in range(200):
        for rule in inputlist:
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
            if "shiny gold" in innerbags:
                canholdgold[outerbag] = 1
            for x in innerbags:
                if x in canholdgold:
                    if canholdgold[x] == 1:
                        canholdgold[outerbag] = 1

            # print(innerbags)
        # print(len(canholdgold))
        # print(len(canholdgold))
    goldholdcount = 0
    for x in canholdgold.values():
        if x == 1:
            goldholdcount += 1
    print(goldholdcount)


p1(inputlist)
# print(set(baglist))
