arr = []

with open('day-1/data.txt') as f:
    __temp_arr = f.readlines()

    for i in range(len(__temp_arr)):
        numstr = __temp_arr[i][:-1]
        arr.append(numstr)

arr.append('')

maxsum = 0
cursum = 0
for i in arr:
    if i != '':
        cursum += int(i)
    else:
        if cursum > maxsum:
            maxsum = cursum
        cursum = 0
print(maxsum)
