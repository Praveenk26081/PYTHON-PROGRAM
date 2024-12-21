names=[]

n=int(input("Enter the number of input"))
for i in range(n):

    name=input(f"Enetr your name {i+1}")
    names.append(name)

order=input("Enter A/D").strip().upper()

if order=='A':

    names.sort()

elif order=='B':

    names.sort(reverse=true)


print("Names in order :")
print()
for name in names:
    print(name)
