import math
def circle(radius):
    area=math.pi*radius*radius
    circumference=2*math.pi*radius
    return area, circumference
r=float(input("Enter radius: "))
area,circumference=circle(r)
print("Area =",area)
print("Circumference =",circumference)