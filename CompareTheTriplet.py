a = list(map(int, input('Enter marks stored by A : ').rstrip().split()))

b = list(map(int, input('Enter marks stored by B : ').rstrip().split()))
    
ap = 0;bp=0
l = [0,0]
for i in range(3):
    if(a[i]>b[i]):
        ap = ap + 1
    if(a[i]<b[i]):
        bp = bp + 1            
l = [ap,bp]
print(str(ap)+' '+str(bp))