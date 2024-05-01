a = input("choose celsius or fahrenheit: ")
if a.lower()=="celsius":
    celsius = float(input("Enter temperature in Celsius: "))
    farenheit = (celsius*9/5) + 32
    print("The temperature in celsius",farenheit)
elif a.lower()=="fahrenheit":
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit-32)* 5/9
    print("The temperature in celsius: ",celsius)
else:
    print("Not a temperature type")
