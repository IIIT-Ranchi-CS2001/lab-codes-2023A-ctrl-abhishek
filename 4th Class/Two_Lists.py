name = [input("Enter name: ").split()]
age = [input("Enter age: ").split()]
gender = [input("Enter gender: ").split()]
income = [input("Enter income: ").split()]
l=len(name)
for i in range(l):
    l.append(name[i]+":"+age[i]+":"+gender[i]+":"+income[i])
print(l)