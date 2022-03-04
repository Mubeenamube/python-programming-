a=int(input("enter a number"))
f=1
if a<0:
    print("factorial not exit")
elif a==0:
    print("factorial is zero")
else:
    for i in range(1, a + 1):
        f=f*i
        print("factorial is",f)