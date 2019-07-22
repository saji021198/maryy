d=int(input())
f=str(d)
decimal=0
for i in range (0,len(f)):
    m=d%10
    h=pow(2,i)
    decimal=decimal+(m*h)
    d=d//10
print(decimal)
