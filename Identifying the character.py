a=input("Enter any character : ")
if a>='A' and a<='Z':
    print("The entered character is uppercase")
elif a>='a' and a<='z':
    print("The entered character is lowercase")
elif a>='0' and a<='9':
    print("The entered character is a digit")
else:
    print("The entered character is a special character")