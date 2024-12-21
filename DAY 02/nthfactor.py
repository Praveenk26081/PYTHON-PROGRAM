num=int(input("Enter the number :"))
facts=[]
if(num>1):
    for i in range (1,num+1):
        
      if(num%i==0):
        facts.append(i)

    print(facts)
    print("The number of factors are :",len(facts))

    n=int(input("Enter the nth fact :"))

    print("the nth factor is :",facts[n-1])


