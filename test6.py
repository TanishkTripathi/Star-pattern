n=5

for i in range(n):
    if i==0:
        print("*"*(n*2-1))
    else:
        print("*"*(n-i)," "*(i*2-1),"*"*(n-i),sep="")