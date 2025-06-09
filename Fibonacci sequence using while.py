n=int(input("Enter the number : "))
a=0
b=1
c=b
count=3
print(a,b,end=" ")
while count<=n:
    print(c,end=" ")
    count+=1
    a,b=b,c
    c=a+b
print()
    