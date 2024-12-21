num=int(input("Enter the number :"))
su=0
rev=0
rem=0
if(num>1):
    for i in range (1,num):
      rem=num%10
      su+=rem
      num=num//10
print("The sum of number is ",su)
