n = int(input("Enter the number: "))
print("Number:",n)
sum = 0
while n>0:
    d=n%10
    sum+=d
    n=n//10
print("Sum of the digits:",sum)