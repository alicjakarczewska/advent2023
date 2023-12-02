filename = 'day2/input2-1.txt'
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
pattern = [12,13,14]

print(len(res_lines))

for i in range(0, len(res_lines)):
    compared = True

    for j in range(0, len(res_lines[i])):
        if(res_lines[i][j] > pattern[j]):
            compared = False
    
    if(compared):
        result += i+1

    print(i,' ',res_lines[i],' ', compared)

print(result)
        

