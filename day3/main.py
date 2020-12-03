import fileinput
mylist = []
for x in fileinput.input():
    mylist.append(x.strip())
#mylist[0][0] is top left
#right 3 is mylist[0][3]
#down 1 is mylist[1][0]
treecounter = 0
def check(dx,dy,mylist):
    y = 0
    i = 0
    treecounter = 0
    while i < len(mylist):
        if mylist[i][y] == '#':
            treecounter += 1
        y = (y + dx) % len(mylist[0])
        i += dy
    return treecounter
print(check(3,1,mylist))
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
countlist = []
for x in slopes:
    countlist.append(check(x[0],x[1],mylist))
    #print(check(x[0],x[1],mylist))
product = 1
for x in countlist:
    product *= x
print("Part 2",product)
