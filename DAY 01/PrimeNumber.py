num= int(input("Enter the Number:" ))

if num>1 :

    for i in range (2,num):
        if num%i==0 :
            print(f"{num} is not a prime number")
            break

        else:
                Print(f"{num} is a prime number")
                

else:
    print(f"{num} is not a prime number")
