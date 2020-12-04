import requests
#get # for day
import sys
with open('secrets.txt', 'r') as f:
    secret = f.read().strip()
#python3 getinput.py {day}
#todo create directorys
#and basic python file if not present
x = sys.argv[1]
cookies = {
        'session': secret
            }

headers = {
        }

response = requests.get(f'http://adventofcode.com/2020/day/{x}/input', headers=headers, cookies=cookies)
print(str(response.content[0:10],'utf-8'))
with open(f'day{x}/input.txt', 'wb') as f:
    if str(response.content[0:3],'utf-8') != "Ple":
        f.write(response.content)
        print("wrote to file")
