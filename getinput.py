import requests
#get # for day
import sys
with open('secrets.txt', 'r') as f:
    secret = f.read().strip()
#python3 getinput.py {day}
x = sys.argv[1]
cookies = {
        'session': secret
            }

headers = {
        }

response = requests.get(f'http://adventofcode.com/2020/day/{x}/input', headers=headers, cookies=cookies)
with open(f'day{x}/input.txt', 'wb') as f:
    f.write(response.content)
