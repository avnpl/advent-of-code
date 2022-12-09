arr = []

with open('day-1/data.txt') as f:
    __temp_arr = f.readlines()

    for i in range(len(__temp_arr)):
        numstr = __temp_arr[i][:-1]
        arr.append(numstr)

arr.append('')

fsum = 0
ssum = 0
tsum = 0
cursum = 0

for i in arr:
    if i != '':
        cursum += int(i)
    else:
        if cursum > fsum:
            tsum = ssum
            ssum = fsum
            fsum = cursum
        elif cursum > ssum:
            tsum = ssum
            ssum = cursum
        elif cursum > tsum:
            tsum = cursum
        cursum = 0

print(fsum + ssum + tsum)
