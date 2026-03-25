# palindrome
a=input("Enter a string: ")
b=""
for i in a:
    b=i+b
if a==b:
    print("Palindrome")
else:
    print("Not a palindrome")