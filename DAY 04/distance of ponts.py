import math

def btdistance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*2+(y2-y1)*2)


x1=float(input("Enter the x1 value"))
x2=float(input("Enter the x2 value"))
y1=float(input("Enter the y1 value"))
y2=float(input("Enter the y2 value"))

distance= btdistance(x1,y1,x2,y2)

print(f"The distance between {x1},{y1} and {x2},{y2} is {distance:.2f}")

