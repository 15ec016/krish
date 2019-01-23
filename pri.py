h=[]
n=[]
k=int(input())
for x in range(k):
    n.append(input().split())
for x in n:
    for y in x:
        h.append(int(y))
h.sort()
s=" ".join(map(str,h))
print(s)
