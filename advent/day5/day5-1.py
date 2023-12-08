import re

# filename = 'day5/input5.txt'
filename = 'day5/input-example.txt'
with open(filename) as f:
    lines = f.read().splitlines()

def get_numbers(str):
    numbers = [(match) for match in re.findall(r'\d+', str)]
    return [int(el) for el in numbers]
# print(lines)
# print(type(lines))

seeds_list = get_numbers(lines[0])
print(seeds_list)




maps = []
map_idx = 0
maps_lines = lines[1:]
print('maps_lines')
print(maps_lines)
# maps_lines = [el for el in lines]
for i, line in enumerate(maps_lines):
    if(':') in line:
        # print('nowa mapa: ', maps_lines[i])

        for j in range(i+1, len(maps_lines)):
            if maps_lines[j] == '':
                map_idx += 1
                break
            # maps.append([maps_lines[j]])


            # print(j,': ', maps_lines[j])
            current_numbers = get_numbers(maps_lines[j])
            if(len(maps)<=map_idx):
                maps.append([current_numbers])
            else:
                maps[map_idx].append(current_numbers)
               
# mapping_list_el = [i for i in range(0,101)]
# mapping_list = [mapping_list_el for i in range(0,9)]

# print('mapping_list')
# for e in mapping_list:
    # print(e)
#     print('m:',m)
# print('maps')
# print(maps)

# str_list = [[i] for i in range(0,101)]

# mapping_list_el = [i for i in range(0,101)]
# new_list = mapping_list_el.copy()


for i, seed in enumerate(seeds_list):
    print('SEEEEED', i)
    for j, map in enumerate(maps):
        print('mapa nr ',j+1)
        for map_el in map:
            start_destination = map_el[0]
            start_source = map_el[1]
            how_many = map_el[2]
            end_source = start_source + how_many

            if(seeds_list[i] >= start_source and seeds_list[i] < end_source):
                print('zmieniamy: ', seeds_list[i],' bo w zakresie: ',start_source,"-",end_source  )
                new_value = start_destination + seeds_list[i] - start_source
                print('nowa wartosc:', new_value)
                seeds_list[i] = new_value
                break
    print('seeds_list')
    print(seeds_list)

result = min(seeds_list)
print('!result!')
print(result)


# def get_new_destination(seed, ):
#     if()


# for i, map in enumerate(maps):
    
#     for map_el in map:
#         print('oto map_el',map_el)
#         start_destination = int(map_el[0])
#         start_source =int(map_el[1])
#         

#         print(start_destination, start_source, how_many)
        
        
        
#         # adder = 0
#         # for k in range(start_source, start_source + how_many):
#         #     new_value = start_destination + adder
#         #     print('dla miejsca: ',k,'o wart:',mapping_list_el[k]," przypiszmy:", new_value)
#         #     new_list = [new_value for el in mapping_list_el if el == k]
#         #     mapping_list_el[k] = new_value
#         #     adder += 1

#     print('zmienione wg mapy nr ',i)
#     print(
#         # '78:' ,mapping_list_el[78],'\n',
#           '79:' ,new_list[79],'\n',
#         #   '13:' ,mapping_list_el[13],'\n',
#           '14:' ,new_list[14],'\n')

# print('mapping_list_el')
# for i,e in enumerate(mapping_list_el):
#     print(i,": ",e)

# for e in str_list:
#     print(e)