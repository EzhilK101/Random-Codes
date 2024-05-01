def sum_multiples(multiple):
    total = 0
    for i in range(multiple):
        if i%3 ==0 or i%5==0:
            total+=i
    return total
result =  sum_multiples(1000)
print("The sum of all multiples of 3 or 5 below 1000 is", result)

