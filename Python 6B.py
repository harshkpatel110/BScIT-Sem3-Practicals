import Python6Bgeometry
def pointyShapeVolume(x,y,squareBase):
    if squareBase:
        print("The area of the base of the square is: ",Python6Bgeometry.squareArea(x))
        return (1/3)*Python6Bgeometry.squareArea(x)*y
    else:
        print("The area of the base of the circle is: ",Python6Bgeometry.circleArea(x))
        return (1/3)*Python6Bgeometry.circleArea(x)*y
squareBase=bool(int(input("What is the type of the shape to calculate volume?\n0. Enter 0 for a right circular cone\n1. Enter 1 for a square base pyramid\n")))
if squareBase:
    x=float(input("Enter the length of the base of the pyramid: "))
    y=float(input("Enter the height of the pyramid: "))
else:
    x=float(input("Enter the radius of the base of the cone: "))
    y=float(input("Enter the height of the cone: "))
print("The volume of the shape is: ",pointyShapeVolume(x,y,squareBase))