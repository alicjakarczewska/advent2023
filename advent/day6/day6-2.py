import re

filename = 'day6/input6.txt'

with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]

def get_str_number(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    new_list = [(el) for el in numbers]
    return int("".join(new_list))

time_nr = get_str_number(lines[0])
distance_nr = get_str_number(lines[1])

# print(time_nr)
# print(distance_nr)

result = 1
mod = time_nr % 2

win = 0
last = 0

for i in range(0, int((time_nr) / 2) + 1):
    res = i * (time_nr - i)
    last = res

    if(res > distance_nr):
        win+=1
        
win*=2

if(not mod and win > 0):
    win -= 1

result *= win

print(result)
    