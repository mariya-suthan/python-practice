# anagram or not
a=input("enter the string : ")
b=input("enter the string : ")
if sorted(a) == sorted(b):
    print("it is an anagram", a,b)
else:
    print("its not an anagram")