a=int(input("enter any number"))
count=0
n1,n2=0,1
if a<0:
    print("enter positive number")
elif a==1:
    print("fibonacci series")
while count<a:
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    count+=1