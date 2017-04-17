ead input from STDIN. Print output to STDOUT
n, m = map(int, raw_input().split())
arr = [0]*n
for i in range(m):
    a,b,k = map(int, raw_input().split())
    arr[a-1] += k
    if b<n:
        arr[b] -= k
       
x = 0
biggest = 0
for i in range(n):
    x += arr[i]
    if x>biggest:
        biggest = x

print biggest
