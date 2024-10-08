
# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to find the nth prime number
def nth_prime(n):
    count = 0  
    number = 1 
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number

# Get input from the user
n = int(input("Enter a number (1 to 15): "))

if 1 <= n <= 15:
    print(f"The {n} prime number is: {nth_prime(n)}")
else:
    print("Please enter a number between 1 and 15.")
