def prime(n):
    if n <= 1:  
        return False  #numbers less than or equal to 1 are not prime
    for i in range (2, int (n**0.5) + 1):
        if n % i == 0:
            return False
    return True  #if no divisors are found, the number is prime

# Example
number = 19
if prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")