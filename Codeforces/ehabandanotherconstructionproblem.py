n = int(input())
l=[]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a%b==0 and a*b>n and a/b<n:
            l.append(a)
            l.append(b)
if len(l)>0:
    print(l[0],l[1])
else:
    print(-1)
            

        