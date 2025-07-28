"""Write a program to accept two numbers as command line arguments 
and display their sum."""
import sys

def sum(num1, num2):
    return num1 + num2 

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
print(sum(num1, num2))


""" Write a program to accept a welcome message through command line
    arguments and display the file name along with the welcome message.
"""
import sys
def welcome_fun(str1):
    return str1 

arg = sys.argv[1]
filename = sys.argv[0]
welcome_message = welcome_fun(arg)
print(f"The file name is: {filename}")
print(f"Welcome: {welcome_message}")


""" Write a program to accept 10 numbers through command line
arguments and calculate the sum of prime numbers among them."""
import sys

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if n % i == 0:
            return False
    return True 

if len(sys.argv) != 11:
    print("Usage: python sum_primes.py num1 num2 ... num10")
    sys.exit(1)
    
numbers = list(map(int, sys.argv[1:]))
prime_sum = sum(i for i in numbers if is_prime(i))
print("Sum of prime numbers:", prime_sum)