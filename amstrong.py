n=int(input("enter a amstrong number"))
a=n
sum1=0
while a!=0:
    temp=a%10
    sum1=sum1+temp**3
    a=a//10
if sum1==n:
    print(" it is amstrong")
else:
    print("not amstrong")

