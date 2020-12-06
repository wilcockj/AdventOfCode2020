import fileinput
mylist = []
seatid = []
seats = []
#FB0-128
for x in fileinput.input():
    mylist.append(x.strip())
#print(mylist[0][0:7])
for boardpass in mylist:
    base = [0,127]
    print(boardpass[0:6])
    for x in boardpass[0:6]:
        print(base,x)
        if x == 'F':
            base[1] = base[1] - ((base[1]-base[0]) // 2 + 1)
        elif x == 'B':
            base[0] = base[0] + ((base[1]-base[0]) // 2 + 1)
        print(base)
    if boardpass[6] == 'F':
        base = [base[0],base[0]]
    elif boardpass[6] == 'B':
        base = [base[1],base[1]]
    print(base)
    row = base[0]
#RL 0-7 R gets 4-7 then L gets 4-5
    base = [0,7]
    for x in boardpass[7:9]:
        print(base,x)
        if x == 'L':
            base[1] = base[1] - ((base[1]-base[0]) // 2 + 1)
        elif x == 'R':
            base[0] = base[0] + ((base[1]-base[0]) // 2 + 1)
        print(base)
    if boardpass[9] == 'L':
        base = [base[0],base[0]]
    elif boardpass[9] == 'R':
        base = [base[1],base[1]]
    col = base[0]
    seatid.append(row*8+col)
    print(boardpass,base)
    seats.append([col,row]) 
    print(base)
print(seats)
columnslist = [[]*7]
for x in seats:
    columnslist[x[0]].append(x[1])

print(columnslist[0]) 
print(max(seatid))
