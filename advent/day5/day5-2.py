import re

# filename = 'day5/input5.txt'
filename = 'day5/input-example.txt'
with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]

seeds_list = get_numbers(lines[0])
# print('seeds_list')
# print(seeds_list)

seeds_ranges = [(seeds_list[i],seeds_list[i]+seeds_list[i+1]) for i in range(0,len(seeds_list),2)]

# print('seeds_ranges')
# print(seeds_ranges)


# find common parts in ranges and minimize them
sorted_ranges = sorted(seeds_ranges)
new_ranges = [sorted_ranges[0]]

for my_range in sorted_ranges[1:]:
    previous_range = new_ranges[-1]

    current_start = my_range[0]
    previous_start = previous_range[0]

    current_end = my_range[1]
    previous_end = previous_range[1]
    
    if current_start <= previous_end:
        updated_previous_range = (previous_start, max(current_end, previous_end))
        new_ranges[-1] = updated_previous_range
    else:
        new_ranges.append(my_range)

print('new_seeds_ranges')
print(new_ranges)

maps = []
map_idx = 0
maps_lines = lines[1:]

for i, line in enumerate(maps_lines):
    if(':') in line:
        # print('nowa mapa: ', maps_lines[i])
        for j in range(i+1, len(maps_lines)):
            if maps_lines[j] == '':
                map_idx += 1
                break
            current_numbers = get_numbers(maps_lines[j])
            if(len(maps)<=map_idx):
                maps.append([current_numbers])
            else:
                maps[map_idx].append(current_numbers)
               
print('all maps:')
print(len(maps))

last_ranges = new_ranges.copy()

for seed_map in maps:
    print('new_ranges')
    print(new_ranges)

    for(start, end) in last_ranges:
        found_mapping = False
        for map_el in seed_map:
            start_destination = map_el[0]
            start_source = map_el[1]
            how_many = map_el[2]
            end_source = start_source + how_many

            print('\nstart_destination: ', start_destination)
            print('start_source: ', start_source)
            print('end_source: ', end_source)
            print('how_many: ', how_many)

            # if current range starts before start_destination
            if(start < start_destination):
                if(end < start_source):
                    # and ends before start_source
                    last_ranges.append((start, end))
                    found_mapping = True
                    break
                if(end <= end_source):
                    last_ranges.append((start, start_source))
                    last_ranges.append((how_many, how_many + end - start_source))
                    found_mapping = True
                    break
                last_ranges.append((start, start_source))
                last_ranges.append((how_many, how_many + end - start_source))
                start = end_source
                break
            elif start_source <= start < end_source:
                if(end <= end_source):
                    last_ranges.append((how_many+start-start_source,how_many+end_source-start_source))
                    start = end_source
                    break
            if not found_mapping:
                last_ranges.append((start, end))
                break
            break
print(last_ranges)
print('!res')
print(min([start for start, _ in last_ranges]))







# seeds = []

# for i in range(0, len(seeds_list), 2):
#     # add the range to the list
#     new_data = (int(seeds_list[i]), int(seeds_list[i]) + int(seeds_list[i+1]))
#     seeds.append(new_data)
# # create list of seed maps
# print('seeds')
# print(seeds)

# for i, seed in enumerate(seeds_list):
#     print('SEEEEED', i)
#     for j, map in enumerate(maps):
#         print('mapa nr ',j+1)
#         for map_el in map:
#             start_destination = map_el[0]
#             start_source = map_el[1]
#             how_many = map_el[2]
#             end_source = start_source + how_many

#             if(seeds_list[i] >= start_source and seeds_list[i] < end_source):
#                 print('zmieniamy: ', seeds_list[i],' bo w zakresie: ',start_source,"-",end_source  )
#                 new_value = start_destination + seeds_list[i] - start_source
#                 print('nowa wartosc:', new_value)
#                 seeds_list[i] = new_value
#                 break
#     print('seeds_list')
#     print(seeds_list)

# result = min(seeds_list)
# print('!result!')
# print(result)

