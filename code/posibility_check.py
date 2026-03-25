# if the input is 10 get the output as 10+0 = 10,9+1=10,8+2=10,7+3=10,6+4=10,5+5=10
a=int(input("enter the number : "))
for i in range(0,a+1):
    print(f"{a-i}+{i}={a}")