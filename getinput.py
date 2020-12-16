import requests
# get # for day
import sys
import os
import glob
with open('secrets.txt', 'r') as f:
    secret = f.read().strip()
# python3 getinput.py {day}
# todo create directorys
# and basic python file if not present
x = sys.argv[1]
cookies = {
    'session': secret
}

headers = {
}

basic = f'''# Advent of Code day {x}
inputlist = []
with open('input.txt','r') as f:
    inputlist = f.readlines()
inputlist = [x.strip('\\n') for x in inputlist]
#if all ints
#inputlist = [int(x) for x in inputlist]
'''
response = requests.get(
    f'http://adventofcode.com/2020/day/{x}/input', headers=headers, cookies=cookies)
print(str(response.content[0:10], 'utf-8'))
if str(response.content[0:3], 'utf-8') != "Ple":
    if not os.path.exists(f'day{x}'):
        os.makedirs(f'day{x}')

    with open(f'day{x}/input.txt', 'wb') as f:
        f.write(response.content)
        print("wrote to file")
    if len(glob.glob(f'day{x}/*.py')) == 0:
        with open(f'day{x}/main.py', 'w') as f:
            f.write(basic)
        print("Made template python file")
