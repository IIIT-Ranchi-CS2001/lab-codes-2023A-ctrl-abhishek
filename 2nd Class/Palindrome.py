str = input("Enter a string: ")
string = str.lower()
palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[-(i + 1)]:
        palindrome = False
        break
if palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")