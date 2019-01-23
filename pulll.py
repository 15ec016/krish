n=int(input())
q=int(input())
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
for j in range(q):
    k=0
    u=int(input())
    v=int(input())
    for i in range(u,v):
        k=k+int(l1[i])
    print(k)
