num=int(input("enter any digit"))
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print(num,"is not a prime number")
            print(i,"times",num)
            break
        else:
            print(num,"is a prime number")