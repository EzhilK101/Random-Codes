def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a
num1 = int(input("Enter a number"))
num2 = int(input("Enter 2nd number"))
result = gcd(num1,num2)
print("GCD of",num1, "and", num2,"is",result)
