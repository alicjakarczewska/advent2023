import re

# filename = 'day7/input.txt'
filename = 'day7/input7.txt'

with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]

input_list=[]

options = "A K Q J T 9 8 7 6 5 4 3 2".split(' ')

def custom_sort(a):
    alphabet = "AKQJT98765432"
    return sorted(a, key=lambda word: [alphabet.index(c) for c in word[0]])

occurences = {}

for i, el in enumerate(options):
    occurences[el] = 0

base_occurences = occurences.copy()

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []
other =[]

for idx, line in enumerate(lines):
    splitted = line.split(' ')
    splitted[1] = int(splitted[1])
    input_list.append(splitted)

    occurences = dict.fromkeys(occurences, 0)
    hand = splitted[0]

    # print(occurences)

    for el in hand: 
        occurences[el] += 1

    # print('\n',hand, 'occurences')
    # print(occurences)

    values = list(occurences.values())

    if(5 in values):
        five_of_kind.append(splitted)
        continue
    if(4 in values):
        four_of_kind.append(splitted)
        continue
    if(3 in values and 2 in values):
        full_house.append(splitted)
        continue
    if(3 in values):
        three_of_kind.append(splitted)
        continue
    if(2 in values):
        count_pairs = values.count(2)
        if(count_pairs == 2):
            two_pair.append(splitted)
        else:
            one_pair.append(splitted)
        continue
    else:
        other.append(splitted)
        
l1 = custom_sort(five_of_kind)
l2 = custom_sort(four_of_kind)
l3 = custom_sort(full_house)
l4 = custom_sort(three_of_kind)
l5 = custom_sort(two_pair)
l6 = custom_sort(one_pair)
l7 = custom_sort(other)

all_lists = [l1,l2,l3,l4,l5,l6,l7]
# print(all_lists)

flat_list = []
for i,l in enumerate(all_lists):
    # print('-----LIST----',i)
    # print(l)
    for el in l:
        flat_list.append(el)
        # print(el)

result = 0

# print('flat')
# print(flat_list)

flat_list.reverse()

for i, f in enumerate(flat_list):
    # print(i)
    # print(f)
    part = f[1] * (i+1)
    result += part
    # print(i+1, ' ', f[0], ' ',f[1])

# print('!result!')
print(result)
