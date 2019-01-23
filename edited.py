a=list(map(int,input().split()))
b=list(map(int,input().split()))
e=[]
for k in range(a[1]):
  c=list(map(int,input().split()))
  d=b[(c[0]-1)]^b[(c[0])]
  for j in range(c[0]+1,c[1]):
    d=d^b[j]
  e.append(d)
for k in range(len(e)):
  print(e[k])
