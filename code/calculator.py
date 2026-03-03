# create calculator using if condition
print("welcome to my calculator")
c=input("enter the method of operation : ")
l_c=c.lower()
if (l_c == "addition"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a+b)
elif (l_c == "subraction"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a-b)
elif (l_c == "multiplication"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a*b)
elif (l_c == "division"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    if(a==0 and b==0):
        print("undefined")
    else:
        print(a/b)
elif (l_c == "floor division"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    if(a==0 and b==0):
        print("undefined")
    else:
        print(a//b)
elif (l_c == "modulas"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    if(a==0 and b==0):
        print("undefined")
    else:
        print(a%b)
elif (c == "exponent"):
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    print(a**b)
else:
    print("use only these command 'addition','subraction','multiplication','division','floor division','modulas','exponent' to perform the operation")