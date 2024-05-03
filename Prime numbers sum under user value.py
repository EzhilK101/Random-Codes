def prime_numbers(limit):
    if limit < 2:
        print("No prime numbers exist for the given limit.")
        return
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def main():
    user_limit = int(input("Enter a number to find prime numbers up to: "))
    prime_list = prime_numbers(user_limit)
    print("Prime numbers up to", user_limit, "are:", prime_list)

if __name__ == "__main__":
    main()
