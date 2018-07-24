def check(l,k):
    li=sorted(li)
    return l[len(li)-k]
    
n=input()
li=[]

if n>0:
    
    k=input()
    if k<=n:
        for x in range(0,n):
            l.append(input())
        print check(l,k)
    else:
        print 'invalid position'
else:
    print 'invalid input'
        
