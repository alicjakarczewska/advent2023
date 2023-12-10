# filename = 'day10/example1.txt'
# filename = 'day10/example2.txt'
filename = 'day10/example3.txt'
# filename = 'day10/input10.txt'

with open(filename) as f:
    lines = f.read().splitlines()

places = []

translated = [l.translate(str.maketrans("-|F7LJ.", "─│┌┐└┘ ")) for l in lines]
for l in translated:
    print(l)

for i,line in enumerate(lines):
    places.append(['.'])
    for j,el in enumerate(line):
        if(el == 'S'):
            # el = 0
            start = (i,j)
        places[i].append(el)
    places[i].append('.')

dots = ['.' for el in range(0,len(lines[0])+2)]
places.insert(0,dots)
places.append(dots)

import copy
copied = copy.deepcopy(places)



start = (start[0]+1,start[1]+1)

for p in places:
    print(p)

print(start)
# for p in places:
#     print(p)
should_end = False
curr = start
res = 0
x = curr[0]
y = curr[1]
prev = 'a'

while(not should_end):
    curr_value = places[x][y]
    curr = (x,y)

    check_r = places[x][y+1]
    check_d = places[x+1][y]
    check_l = places[x][y-1]
    check_u = places[x-1][y]


    print('\n\n----curr_value----')
    print(curr_value)
    print('curr x y')
    print(curr)
    print('check_r')
    print(check_r)

    print('check_d')
    print(check_d)


    print('check_u')
    print(check_u)


    print('check_l')
    print(check_l)

    

    if(curr_value in ['S','L','F','-'] and check_r in ['-','7','J','S'] and prev != 'r'):
        print('1) hello')
        y=y+1
        prev='l'
    elif(curr_value in ['S','J','7','-'] and check_l in ['-','L','F','S']and prev != 'l'):
        print('2) hello')
        prev='r'
        y=y-1
    elif(curr_value in ['S','L','J','|'] and check_u in ['|','7','F','S'] and prev != 'u'):        
        print('3) hello')
        prev='d'
        x=x-1
    elif(curr_value in ['S','F','7','|'] and check_d in ['|','J','L','S']and prev != 'd'):
        print('4) hello')
        prev='u'
        x=x+1
    
    print('next:', places[x][y], 'nowy x:',x,'nowy y:',y)
    res += 1
    # if(res == 10):
    if(places[x][y] == 'S'):
        should_end = True
    copied[x][y] = 'X'

print('ended!')
print('next:', curr, ' x:',x,' y:',y)
print(res)
print('end res')
print(res/2)

new_res = 0

for i, c in enumerate(copied):
    for j, el in enumerate(c):
        if(el == '.'):
            print('\n\nkropka')
            print(i,j)
            x_l = False
            x_r = False
            x_u = False
            x_d = False
            for k in range(j, len(c)):
                print('prawo')
                print(places[i][k])
                if(places[i][k] in ['7','J','|']):
                    x_r = True
            for k in range(0, j):
                print('lewo')
                print(places[i][k])
                if(places[i][k] in ['F','L','|']):
                    x_l = True
            for k in range(0, i):
                print('do gory')
                print(places[k][j])
                if(places[k][j] in ['S','F','7','-']):
                    x_u = True
            for k in range(i, len(copied)):
                print('do dolu')
                print(places[k][j])
                if(places[k][j] in ['L','J','-']):
                    x_d = True
            if(x_l and x_r and x_d and x_u):
                copied[i][j] = 'O'
                new_res += 1

# for i, c in enumerate(copied):
#     for j, el in enumerate(c):
#         if(el == '.'):
#             print('kropka')
#             x_l = False
#             x_r = False
#             x_u = False
#             x_d = False
#             for k in range(j, len(c)):
#                 if(copied[i][k] == 'X'):
#                     x_r = True
#             for k in range(0, j):
#                 if(copied[i][k] == 'X'):
#                     x_l = True
#             for k in range(0, i):
#                 if(copied[k][j] == 'X'):
#                     x_u = True
#             for k in range(i, len(copied)):
#                 if(copied[k][j] == 'X'):
#                     x_d = True
#             if(x_l and x_r and x_d and x_u):
#                 copied[i][j] = 'O'
#                 new_res += 1

# for i, c in enumerate(copied):
#     for j, el in enumerate(c):
#         if(el == 'O'):
#             print('kolko')
#             l = copied[i-1][j]
#             r = copied[i+1][j]
#             u = copied[i][j-1]
#             d = copied[i][j+1]
#             if(l == '.' or r == '.' or u=='.' or d=='.'):
#                 copied[i][j] = '.'
#                 new_res -= 1

#                 if(l == 'O'):
#                     copied[i-1][j] = '.'
#                     new_res -= 1
#                 if(r == 'O'):
#                     copied[i+1][j] = '.'
#                     new_res -= 1
#                 if(u == 'O'):
#                     copied[i][j-1] = '.'
#                     new_res -= 1
#                 if(d == 'O'):
#                     copied[i][j+1] = '.'
#                     new_res -= 1

#  ---------
                    
            

# for i, c in enumerate(copied):
#     for j, el in enumerate(c):
#         if(el == '.'):
#             print('kropka')
#             print(c[j-1], copied[i-1][j], copied[i-1][j-1])
#             if(c[j-1] in ['X','O'] and copied[i-1][j] in ['X','O'] and copied[i-1][j-1] in ['X','O']):
#                 copied[i][j] = 'O'
#                 new_res += 1

# for i, c in enumerate(copied):
#     for j, el in enumerate(c):
#         if(el == 'O'):
#             print('kolko')
#             # print(c[j-1], copied[i-1][j], copied[i-1][j-1])
#             if(not(c[j+1] in ['X'] or copied[i+1][j] in ['X'] and copied[i+1][j+1] in ['X'] and copied[i+1][j+1] in ['X'])):
#             # if(c[j-1] in ['X','O'] and copied[i-1][j] in ['X','O'] and copied[i-1][j-1] in ['X','O'] and not(c[j+1] in ['X'] or copied[i+1][j] in ['X'] and copied[i+1][j+1] in ['X'])):
#                 copied[i][j] = '.'
#                 new_res-=1

for c in copied:
    print(c)


print('new_res')
print(new_res)

