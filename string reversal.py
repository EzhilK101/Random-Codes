txt = str(input("Enter a string"))
if txt == txt[::-1]:
    print(txt,"is palindrome")
else:
    print(txt,"is not palindrome")
