name = str(input("Enter your name: "))
Roll = int(input("Enter your roll number: "))
Marks = int(input("Enter your marks: "))
if(Marks>=90):
    G = 10
    R = "OUTSTANDING"
elif(90>Marks>=80):
    G = 9
    R = "VERY GOOD"
elif(80>Marks>=70):
    G = 8
    R = "GOOD"
elif(70>Marks>=60):
    G = 7
    R = "AVERAGE"
elif(60>Marks>=50):
    G = 6
    R = "PASS"
else:
    G = 0
    R = "FAIL"
print("\nRESULT:-")
print("Name:",name)
print("Roll Number:",Roll)
print("Marks:",Marks)
print("Grade Point:",G)
print("Remark:",R)