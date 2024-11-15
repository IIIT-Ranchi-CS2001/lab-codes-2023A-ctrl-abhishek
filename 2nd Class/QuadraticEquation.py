import math
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = (b**2) - 4*a*c
print(d)
if(d==0):
    r1 = (-b)/(2*a)
    print("The equation has two same real roots.\nRoot1 = Root2 =",r1)
elif(d>0):
    r1 = ((-b)+math.sqrt(d))/2*a
    r2 = ((-b)-math.sqrt(d))/2*a
    print("The equation has two distinct real roots.\nRoot1 =",r1)
    print("Root2 =",r2)
else:
    print("The equation has two complex roots.")
    rp = (-b)/(2*a)
    ip = (math.sqrt(-d))/(2*a)
    print("Root1 =",rp)
    print("+ i",ip)