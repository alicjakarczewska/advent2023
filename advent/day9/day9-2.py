import re

filename = 'day9/input9.txt'
# filename = 'day9/input.txt'


with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]

num_lists = []

for l in lines:
    str_line =  l.split(' ') 
    print('str_line')
    print(str_line)
    int_line = [int(el) for el in str_line]
    num_lists.append(int_line)


print('num_lists')
print(num_lists)

prev_elements = []

for num_list in num_lists:
    print('------')
    diff_lists = []
    end = False
    list_to_check = num_list
    diff_lists.append(num_list)


    while(not end):
        diff = [(list_to_check[i+1] - list_to_check[i]) for i in range(0,len(list_to_check)-1)]
        diff_lists.append(diff)
        list_to_check = diff
        print('list_to_check')
        print(list_to_check)
        print('diff')
        print(diff)


        if(diff.count(diff[0])==len(diff) and diff[0] == 0):
            end = True
 
    print('\n---')
    reversed_diff_lists = diff_lists[::-1]

    next_el = 0
    for idx, curr_list in enumerate(reversed_diff_lists):
        if(idx==0):
            curr_list.insert(0, 0)
            continue
        prev_el = curr_list[0] - reversed_diff_lists[idx-1][0]
        # print('curr_list[-1] ',curr_list[-1])
        # print('reversed_diff_lists[idx-1][-1] ',reversed_diff_lists[idx-1][-1])
        print('prev: ',prev_el)
        curr_list.insert(0, prev_el)

        print('curr_list')
        print(idx,curr_list)

    prev_elements.append(prev_el)

print('prev_elements')
print(prev_elements)
print('!result!')
print(sum(prev_elements))