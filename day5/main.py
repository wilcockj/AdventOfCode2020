import fileinput
mylist = []
seatid = []
seats = []
#FB0-128
for x in fileinput.input():
    mylist.append(x.strip())
for boardpass in mylist:
    base = [0,127]
    for x in boardpass[0:6]:
        if x == 'F':
            base[1] = base[1] - ((base[1]-base[0]) // 2 + 1)
        elif x == 'B':
            base[0] = base[0] + ((base[1]-base[0]) // 2 + 1)
        print(base)
    if boardpass[6] == 'F':
        base = [base[0],base[0]]
    elif boardpass[6] == 'B':
        base = [base[1],base[1]]
    row = base[0]
#RL 0-7 R gets 4-7 then L gets 4-5
    base = [0,7]
    for x in boardpass[7:9]:
        if x == 'L':
            base[1] = base[1] - ((base[1]-base[0]) // 2 + 1)
        elif x == 'R':
            base[0] = base[0] + ((base[1]-base[0]) // 2 + 1)
    if boardpass[9] == 'L':
        base = [base[0],base[0]]
    elif boardpass[9] == 'R':
        base = [base[1],base[1]]
    col = base[0]
    seatid.append(row*8+col)
    seats.append([col,row]) 
seatid = sorted(seatid)
for x,y in enumerate(seatid):
    if x != y-96:
        print(y-1)
        break
print(max(seatid))
