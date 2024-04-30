def interest(principal,rate,time):
    loan= (principal*rate*time)/100
    return loan
principal_1 = float(input("Enter your principal value"))
rate_1 = float(input("Enter your annual interest rate"))
time_1 = float(input("Enter your time period in years"))
simple_interest = interest(principal_1,rate_1,time_1)
print("Simple interest",simple_interest)

    
