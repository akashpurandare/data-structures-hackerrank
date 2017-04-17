ead input from STDIN. Print output to STDOUT

n, nq = map(lambda x: int(x), raw_input().split(" "))
arr = [[] for i in range(n)]
lastAns = 0

def query1(x, y):
    global lastAns, n, arr
    ind = (x^lastAns)%n
    arr[ind].append(y)

    
def query2(x, y):
    global lastAns, n, arr
    ind = (x^lastAns)%n
    #print ind
    lastAns = arr[ind][y%len(arr[ind])]
    print lastAns
    #print arr[ind][lastAns]

for i in range(nq):
    q, x, y = map(lambda x: int(x), raw_input().split(" "))
    if q==1:
        query1(x, y)
    elif q==2:
        query2(x, y)
