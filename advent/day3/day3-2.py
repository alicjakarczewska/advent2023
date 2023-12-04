import re
from functools import reduce

filename = 'day3/input3.txt'

with open(filename) as f:
    lines = f.read().splitlines()


numbers = [*range(0,10)]
numbers = [str(el) for el in numbers]

allowed_places = []

def generate_neighbours(i,j):
    allowed = [[i-1,j-1],[i,j-1],[i+1,j-1],
               [i-1,j],[i+1,j],
               [i-1,j+1],[i,j+1],[i+1,j+1]
               ]
    return allowed

other_characters=[]

stars = []

for i in range(0,len(lines)):
    line = lines[i]
    for j in range(0,len(line)):
        character = lines[i][j]
        other_characters.append(character)
        if(character == '*'):
            new_allowed_places = generate_neighbours(i,j)
            stars.append((i,j,new_allowed_places))
            allowed_places.extend(new_allowed_places)

list_to_check = []

already_existed_places = []
for i in range(0,len(lines)):
    line = lines[i]
    line_numbers = [(match) for match in re.findall(r'\d+', line)]

    for line_number in line_numbers:
        starts = [m.start() for m in re.finditer(line_number, line)]
        digits_nr = len(str(line_number))
            
        for start in starts:
            number_places = []          
            for j in range(0,digits_nr):
                place = [i, start+j]
                not_to_add = False

                if(place in already_existed_places):
                    for idx, el in enumerate(list_to_check):
                        if(place in el[1]):
                            if(int(el[0])>=int(line_number)):
                                not_to_add = True
                            if(int(el[0])<int(line_number)):
                                list_to_check[idx][1].remove(place)
            
                if not_to_add:
                    not_to_add=False
                    break
                else:
                    number_places.append([i, start+j])

                
            if(number_places is not []):
                list_to_check.append([line_number, number_places])
        
            already_existed_places.extend(number_places)


result = 0

allowed_numbers = []
for i in list_to_check:
    allowed_numbers.append(i[0])

not_allowed = []

star_numbers = {}

for i in list_to_check:
    checked_number = i[0]
    places = i[1]
    for place in places:
        found = 0
        if(place in allowed_places):
            for star in stars:
                if(place in star[2]):
                    if star_numbers.get((star[0],star[1])) is not None:
                        star_numbers[(star[0],star[1])].append(checked_number)
                    else:
                        star_numbers[(star[0],star[1])] = [checked_number]
                    found = 1
            if(found):
                break
            result += int(checked_number)
            found = 1
            break
    if(found == 0):
        not_allowed.append(checked_number)

result = 0
for el in star_numbers:
    num = star_numbers[el]
    num = [int(el) for el in num]
    if len(num) > 1:
        # print(num)
        part = reduce(lambda x, y: x*y, num)
        result+=part

print(result)

        


