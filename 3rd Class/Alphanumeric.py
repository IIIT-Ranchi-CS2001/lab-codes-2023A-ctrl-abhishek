def alphanumeric(s):
    for char in s:
        if not char.isalnum():
            print(False)
            return
    print(True)

n = input("Enter the string: ")
alphanumeric(n)