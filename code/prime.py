#prime or not
a=int(input("enter the number : "))
if a<=1:
    print("not prime")
else:
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            print("not prime")
            break
    else:
        print("prime")