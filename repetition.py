p=int(input())
l=str(p)
c=0
for i in range (0,len(l)):
    for j in range(1,len(l)):
        if(l[i]==l[j]):
            c=1
            break
        else:
            i=i+1
if(c==1):
    print("yes")
else:
    print("no")

