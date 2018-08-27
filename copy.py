b=list("string");
for i in range(0,len(b)):
    if (i%2==0) and ((i+1)%2!=0):
        temp=b[i];
        b[i]=b[i+1];
        b[i+1]=temp;
        
    res="".join(b)
    print res
