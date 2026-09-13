import math
def volume(x,y,squareBase):
    if squareBase:
        return (x*x*y)/3
    else:
        return (math.pi*x*x*y)/3
choice=int(input("1. Square Pyramid\n2. Cone\nEnter your choice: "))
if choice==1:
    side=float(input("Enter side: "))
    height=float(input("Enter height: "))
    print("Volume =",volume(side,height,True))
elif choice==2:
    radius=float(input("Enter radius: "))
    height=float(input("Enter height: "))
    print("Volume =",volume(radius,height,False))
else:
    print("Invalid Choice")