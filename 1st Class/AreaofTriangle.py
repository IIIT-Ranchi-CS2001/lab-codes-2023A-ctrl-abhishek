import math
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
s = (a+b+c)/2
x = math.sqrt(s*(s-a)*(s-b)*(s-c))
p = 2*s
print("Perimeter of the triangle is",p)
print("Area of the triangle is",x)
i = math.degrees(math.acos(((b**2) + (c**2) - (a**2))/(2*b*c)))
j = math.degrees(math.acos(((a**2) + (c**2) - (b**2))/(2*a*c)))
k = math.degrees(math.acos(((a**2) + (b**2) - (c**2))/(2*a*b)))
print("Angle A is",i)
print("Angle B is",j)
print("Angle C is",k)