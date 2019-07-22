p=int(input())
uu=str(p)
c=0
for i in range (0,len(uu)):
    for j in range(1,len(uu)):
        if(uu[i]==uu[j]):
            c=1
            break
        else:
            i=i+1
    break
if(c==1):
    print("yes")
else:
    print("no")

