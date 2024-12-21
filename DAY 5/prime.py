a=int(input("Enter the number : "))
c=[]
d=[1,2,3]
if (2<a):
    for i in range(4,a):
        if(i%2==0):
            c.append(i)
        elif(i%3==0):
            c.append(i)
        else:
            d.append(i)

print("not prime ",c)
print("prime :",d)

    
  
         
  
