n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
(r,l) = (0,0)
for i in range(n):
    for j in range(n):
        if(i==j):
            l = l + arr[i][j]
        if((n-1) == (i+j)):
            r = r + arr[j][i]
(r,l) = (max(r,l),min(r,l))
difff = r-l
print(difff)