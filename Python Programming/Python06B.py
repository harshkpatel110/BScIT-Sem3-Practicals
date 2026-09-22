import Python06Bgeometry
choice=int(input("1. Square\n2. Circle\nEnter your choice: "))
if choice==1:
    side=float(input("Enter side: "))
    print("Area =",Python06Bgeometry.squareArea(side))
elif choice==2:
    radius=float(input("Enter radius: "))
    print("Area =",Python06Bgeometry.circleArea(radius))
else:
    print("Invalid Choice")