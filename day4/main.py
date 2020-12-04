import fileinput
import re

def inrange(s,l,h):
    return l<=int(s)<=h
d = []
for x in fileinput.input():
    d.append(x.strip())
s = ""
l = []
for x in range(len(d)):
    if d[x] != '':
        s = s + " " + d[x]
    else:
        l.append(s.lstrip())
        s = ''
    if x == len(d)-1:
        l.append(s.lstrip())
lod = []
for x in range(len(l)):
    lod.append({})
    for y in l[x].split():
        #make dict with key:value
        lod[x][y.split(':')[0]] = y.split(':')[1]
p2count = 0
for x in lod:
    valid = True
    keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    if not all(k in x for k in keys):
        #invalid
        valid = False
    else:
        for rule in x.items():
            if rule[0] == 'byr' and not inrange(rule[1],1920,2002):
                valid = False
            elif rule[0] == 'iyr' and not inrange(rule[1],2010,2020):
                valid = False
            elif rule[0] == 'eyr' and not inrange(rule[1],2020,2030):
                valid = False
            elif rule[0] == 'hgt':
                r = re.compile('(\d+)(\w+)')
                exp = r.match(rule[1])
                ht = exp.group(1)
                msr = exp.group(2)
                if msr == 'cm' and not inrange(ht,150,193):
                    valid = False
                elif msr == 'in' and not inrange(ht,59,76):
                    valid = False
                if msr != 'cm' and msr != 'in':
                    valid = False
            elif rule[0] == 'hcl':
                exp = re.compile('(#[0-9,a-f]{6})')
                res = exp.match(rule[1])
                if not res:
                    valid = False
            elif rule[0] == 'ecl':
                colors = ['amb','blu','brn','gry','grn','hzl','oth']
                if rule[1] not in colors:
                    valid = False
            elif rule[0] == 'pid':
                if len(str(rule[1])) != 9:
                    valid = False
    if valid:
        p2count += 1

        
    
p1count = 0
for x in lod:
    if all(k in x for k in keys):
        #print(x)
        p1count += 1

print("Part 1:",p1count)
print("Part 2:",p2count)
