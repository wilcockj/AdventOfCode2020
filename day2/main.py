#initial
inputlist = []
with open("input.txt","r") as f:
    for line in f:
        inputlist.append(line)
correctpasswords = 0
for line in inputlist:
    policy = [line.split()[0], line.split()[1].replace(':','')]
    policymin = policy[0].split('-')[0]
    policymax = policy[0].split('-')[1]
    password = line.split()[2]
    counter = 0
    for x in range(len(password)):
        if password[x] == policy[1]:
            counter += 1
    if int(policymin) <= counter <= int(policymax):
        correctpasswords += 1

print("part 1:",correctpasswords)
correctpasswords = 0
for line in inputlist:
    policy = [line.split()[0], line.split()[1].replace(':','')]
    policymin = policy[0].split('-')[0]
    policymax = policy[0].split('-')[1]
    password = line.split()[2]
    if password[int(policymin)-1] == policy[1] and password[int(policymax)-1] != policy[1]:
        correctpasswords += 1
        #print(f"{policy} and {password}")
    elif password[int(policymin)-1] != policy[1] and password[int(policymax)-1] == policy[1]:
        correctpasswords += 1
        #print(f"{policy} and {password}")
print("part 2:",correctpasswords)


