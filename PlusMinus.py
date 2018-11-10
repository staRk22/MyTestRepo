num = int(input())
arr = list(map(int, input().rstrip().split()))
(p,n,z)=(0,0,0)
for i in range(num):
    if(arr[i] > 0):
        p = p + 1
    else:
        if(arr[i] < 0):
            n = n + 1
        else:
            z = z + 1
(p,n,z) = (p/num,n/num,z/num)
print(p)
print(n)
print(z)