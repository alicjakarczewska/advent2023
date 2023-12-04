import re

filename = 'day4/input4.txt'
with open(filename) as f:
    lines = f.read().splitlines()

# print(lines)

result = 0

for i,line in enumerate(lines):
    splitted = line.split(':')

    num_lists = splitted[1].split('|')
    # print(num_lists[1])

    winning_numbers = [(match) for match in re.findall(r'\d+', num_lists[0])]
    my_numbers = [(match) for match in re.findall(r'\d+', num_lists[1])]

    power = -1
    count_res = False
    for my_number in my_numbers:
        if(my_number in winning_numbers):
            power += 1
            count_res = True
    if(count_res):
        result += 2**power
    
    # print(i, " counts? ", count_res, " power: ", power, " result: ",result)


    # print(len(winning_numbers),winning_numbers)
    # print(len(my_numbers),my_numbers)
print(result)