ead input from STDIN. Print output to STDOUT

def shift(arr):
    temp = arr[0]
    del arr[0]
    arr.append(temp)

    
def nshift(arr, d):
    global n
    num = d%n
    for i in range(num):
        shift(arr)

n, d = map(lambda x: int(x), raw_input().split(" "))
arr = map(lambda x: int(x), raw_input().split(" "))
nshift(arr, d)
for i in arr:
    print i,

