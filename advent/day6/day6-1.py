import re

filename = 'day6/input6.txt'
# filename = 'day6/input6.txt'

with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]

time_list = get_numbers(lines[0])
distance_list = get_numbers(lines[1])

# print(time_list)
# print(distance_list)

result = 1

for t_idx,time in enumerate(time_list):
    spr = time%2
    win = 0
    last = 0
    for i in range(0, int((time)/2)+1):
        res = i*(time-i)
        last=res
        if(res>distance_list[t_idx]):
            win+=1
    win*=2
    if(not spr and win>0):
        win -= 1
    result *= win

print(result)
    