filename = 'day2/input2-2.txt'
with open(filename) as f:
    lines = f.read().splitlines()

res_lines = []

for line in lines:
    maxblue = 0
    maxred = 0
    maxgreen = 0
    line = line.split()
    for i in range(0,len(line)):
        if('blue' in line[i]):
            maxblue = max(maxblue, int(line[i-1]))
        if('red' in line[i]):
            maxred = max(maxred, int(line[i-1]))
        if('green' in line[i]):
            maxgreen = max(maxgreen, int(line[i-1]))
    res_lines.append([maxred, maxgreen, maxblue])

result = 0

for res_line in res_lines:
    power = res_line[0]*res_line[1]*res_line[2]
    # print(power)
    result += power

print(result)

        

