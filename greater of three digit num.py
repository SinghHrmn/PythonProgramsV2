n=int(input("enter a 3 digt num"))
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10


if a>b and a>c:
    print(a,"is the largest")
elif b>c and b>a:
    print(b,"is the largest")
else:
    print(c,"is the largest")
