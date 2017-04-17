mport sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

def sum_hourglass(arr):
    res = 0
    for i in range(len(arr)):
        if i==3 or i==5:
            pass
        else:
            res += arr[i]
    return res

def create_hourglass(arr,x,y):
    new_arr = []
    count = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            new_arr.append(arr[i][j])
    return new_arr

max = 0

for i in range(4):
    for j in range(4):
        hg = create_hourglass(arr, i, j)
        res = sum_hourglass(hg)
        if (i,j)==(0,0):
            max = res
        elif res>=max:
            max = res

print max
