lower=int(input("Enter the number from where you want to start : "))
upper=int(input("Enter the number till where you want to end   : "))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)