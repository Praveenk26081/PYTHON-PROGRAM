num=int(input("Enter the number :"))
Sum=0
rem=0
temp=num
if(num>1):
    for i in range (1,num):
        
      rem=num%10
      Sum+=rem*rem*rem
      num=num//10
      
    if Sum==temp:
     print("Armstrong Number")
    else:
     print("Not a Armstrong Number")


