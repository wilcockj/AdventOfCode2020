numlist = []
with open("input.txt","r") as f:
    for line in f:
        numlist.append(line.strip('\n'))
print(numlist)
myset = set(int(i) for i in numlist)
print(myset)
#for each number check every other number
def dothing(numlist):
    for count,num in enumerate(numlist):
        currentnum = num
        currentindex = count
        for x in range(len(numlist)):
            for y in range(len(numlist)):
                currentsum = int(currentnum)+int(numlist[x])+int(numlist[y])
                if currentsum == 2020:
                    print("found 2020")
                    print(f"{int(currentnum)} + {int(numlist[x])} + {int(numlist[y])} = {currentsum}")
                    print(int(currentnum)*int(numlist[x])*int(numlist[y]))
                    break
import timeit
print(timeit.timeit(lambda: dothing(numlist),number = 1))

