n1 = int(input("Enter a number"))
op = input('Enter operator (+,-,*,/,^): ')
n2 = int(input("Enter a number"))
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op =='/':
    print(n1%n2)
elif op =='*':
    print(n1*n2)
elif op =='^':
    print(n1^n2)
    
else:
    print("Not valid operator")
    
