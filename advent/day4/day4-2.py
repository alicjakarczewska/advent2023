import re

filename = 'day4/input4.txt'
with open(filename) as f:
    lines = f.read().splitlines()

new_lines = []

for i, line in enumerate(lines):
    splitted = line.split(':')
    num_lists = splitted[1].split('|')

    winning_numbers = [(match) for match in re.findall(r'\d+', num_lists[0])]
    my_numbers = [(match) for match in re.findall(r'\d+', num_lists[1])]

    new_lines.append([winning_numbers, my_numbers])

copies = [[i, 1] for i,line in enumerate(lines)]

# for c in copies:
#     print(c)

for i, new_line in enumerate(new_lines):
    my_numbers = new_lines[i][0]
    winning_numbers = new_lines[i][1]

    occurences = 0
    for my_number in my_numbers:
        if(my_number in winning_numbers):
            occurences += 1
    
    # print('current: ', i, my_numbers, occurences)
    for j in range(i + 1, i + occurences + 1):
        copies[j][1] += copies[i][1]
    
# for c in copies:
#     print(c)
    
result = sum([el[1] for el in copies])
print(result)