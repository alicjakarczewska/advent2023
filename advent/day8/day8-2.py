import re

filename = 'day8/example2.txt'
# filename = 'day8/input8.txt'

with open(filename) as f:
    lines = f.read().splitlines()

my_order = lines[0]
my_order = my_order.replace('L','0').replace('R','1')
print(my_order)
my_list = []
only_first_list=[]

for i, line in enumerate(lines[2:]):
    # print(i, line)
    values = line.split(" = ")
    first = values[0]
    only_first_list.append(first)
    sec = (values[1][1:4],values[1][6:9])
    # print(sec[0])
    # print(sec[1])
    my_list.append([first, sec])

# curr = my_list[0]


order_length = len(my_order)
# visited = []


starting_nodes = list(filter(lambda el: el[2] == 'A', only_first_list))
res_list = []

for node in starting_nodes:
    order_idx = 0
    res = 0
    start_idx = only_first_list.index(node)
    curr = my_list[start_idx]


    while(curr[0][2] != 'Z'):
        # print('\njestem tu:')
        res += 1
        # print(curr)
        # print('order_idx',order_idx)
        way_to_go = int(my_order[order_idx])
        # print('way_to_go')
        # print(way_to_go)
        new_el = curr[1][way_to_go]
        # print('nowy:',new_el)
        # print('find:' ,only_first_list.index(new_el))
        found_idx = only_first_list.index(new_el)
        idx = found_idx
        curr = my_list[idx]
        order_idx += 1
        order_idx %= order_length
    
    print('res: ', node)
    print(res)
    res_list.append(res)

print('res_list')
print(res_list)

import math
lcm_result = math.lcm(*res_list)

print('res_list lcm')
print(lcm_result)

