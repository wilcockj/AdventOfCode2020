# Advent of Code day 17
from itertools import combinations
from itertools import permutations  
from collections import Counter
inputlist = []
with open('input.txt','r') as f:
    inputlist = f.readlines()
inputlist = [x.strip('\n') for x in inputlist]
#if all ints
#inputlist = [int(x) for x in inputlist]
cubedict = {}
#key is z points to list of rows and columns
#[z,[list]]
#['....###.#.', '.#.#.##...', '.##.##..', '..##...#', '.###.##.', '.#..##..', '.....###', '.####..#']
# add inactive all around
#['.*len(cube[0])+2]
def addsurroundingblank(inputlist):
    for count, x in enumerate(inputlist):
        inputlist[count] = '.' + inputlist[count] + '.'
    inputlist.insert(0,'.' * len(inputlist[0]))
    inputlist.append('.' * len(inputlist[0]))
    return inputlist

def addblankz(cubedict):
    maxz = max(cubedict.keys())
    cubedict[maxz+1] = ['.'*len(cubedict[0][0])]*len(cubedict[0])
    cubedict[-maxz-1] = ['.'*len(cubedict[0][0])]*len(cubedict[0])
    return cubedict
inputlist = addsurroundingblank(inputlist)
count = 0
neighbors = []
for x,y,z in [(i,j,k) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) if i != 0 or j != 0 or k != 0]:
        neighbors.append([x,y,z])
#add inactive layer on either side of cube slice
#print(['.'*len(inputlist[0])]*len(inputlist))
cubedict[0] = inputlist
cubedict = addblankz(cubedict)
'''
maxz = max(cubedict.keys())
cubedict[maxz+1] = ['.'*len(cubedict[0][0])]*len(cubedict[0])
cubedict[-maxz-1] = ['.'*len(cubedict[0][0])]*len(cubedict[0])
'''
for x in range(6):
    newdict = {}
    for key,values in cubedict.items():
        count = 0
        for row,value in enumerate(values):
            #have to know row, col\
            #key is z
            for col,state in enumerate(value):
                count = 0
                for neighbor in neighbors:
                    #use z, neighbor[2] for key of dict
                    x,y,z = (neighbor[0],neighbor[1],neighbor[2])
                    if key+z in cubedict and row+x >= 0 and row+x <= len(value)-1 and col+y >= 0 and col+y <= len(value)-1:
                        #print((key+z,row+x,col+y),cubedict[key+z][row+x][col+y])
                        #print(row+x,col+y)
                        if cubedict[key+z][row+x][col+y] == '#':
                            count += 1
                #if (key,row,col) == (0,1,7):
                    #print(f"neighbors at {(key,row,col)} = {count}")

                if key not in newdict:
                    #print("yeah")
                    newdict[key] = ['.' * len(value)]*len(values)

                if cubedict[key][row][col] == '#':
                    #print(f"neighbors at {(key,row,col)} = {count}")
                    if count == 2 or count == 3:
                        #print("kept one active")
                        #print(newdict[key][row][col])
                        fixedrow = list(newdict[key][row])
                        fixedrow[col] = '#'
                        fixedrow = "".join(fixedrow)
                        newdict[key][row] = fixedrow
                    else:
                        #print("made active inactive")
                        #print(newdict[key][row][col])
                        fixedrow = list(newdict[key][row])
                        fixedrow[col] = '.'
                        fixedrow = "".join(fixedrow)
                        newdict[key][row] = fixedrow
                else:
                    if count == 3:
                        #print("made inactive active")
                        fixedrow = list(newdict[key][row])
                        fixedrow[col] = '#'
                        fixedrow = "".join(fixedrow)
                        newdict[key][row] = fixedrow
        
    cubedict = newdict
    for key,values in cubedict.items():
        #print(values)
        cubedict[key] = addsurroundingblank(cubedict[key])
    cubedict = addblankz(cubedict)
    #(0,1,7)=3
    
    #print(count)(0, 1, 8) #
    
#print(cubedict)
activecount = 0
for key,value in cubedict.items():
    for row in value:
        activecount += Counter(row)['#']

print("P1", activecount)