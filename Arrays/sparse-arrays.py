ead input from STDIN. Print output to STDOUT
n = int(raw_input())
str_arr = []
num_arr = []
for i in range(n):
    string = raw_input()
    if string in str_arr:
        for i in range(len(str_arr)):
            if str_arr[i]==string:
                break
        num_arr[i] += 1
    else:
        str_arr.append(string)
        num_arr.append(1)
q = int(raw_input())
for i in range(q):
    query = raw_input()
    if query not in str_arr:
        print 0
    else:
        for i in range(len(str_arr)):
            if str_arr[i]==query:
                print num_arr[i]
