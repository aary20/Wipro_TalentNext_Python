#1. Write a program to check if a given number is Positive, Negative or Zero.
def check_num(num):
    if num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    else:
        return "Positive"
num = int(input("Enter a number: "))
result = check_num(num)
print(f"The number is: {result}")



#2. Write a program to check if a given number is odd or even.
def even_odd_num(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = even_odd_num(num)
print(f"The number {num} is {result}.")




#3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
def same_last_digit(num1, num2):
    last_num1 = num1 % 10
    last_num2 = num2 % 10
    if last_num1 == last_num2:
        return True
    return False
num1 = int(input())
num2 = int(input())
result = same_last_digit(num1, num2)
print(result)



#4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
def num_row():
    for i in range(1, 11):
        print(i, end='\t')
num_row()



#5. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
def even_num():
    for i in range(23, 58):
        if i % 2 == 0:
            print(i, end = '\n')
    return ""
even_num()



#6. Write a program to check if a given number is prime or not.
def prime(num):
    if num < 2:
        return "Not a prime number"
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Not a prime number"
        return "Prime number"
num = int(input())
print(prime(num))



#7. Write a program to print prime numbers between 10 and 99.
def prime_num(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def print_primes_10_99():
    for i in range(10, 100):
        if prime_num(i):
            print(i, end = " ")
print_primes_10_99()



#8. Write a program to print the sum of all the digits of a given number.
def sum_of_digits(num):
    sum_digit = 0
    while num > 0:
        digit = num % 10
        sum_digit += digit
        num //= 10
    print("Sum of digits:", sum_digit)
num = int(input())
sum_of_digits(num)



#9. Write a program to reverse a given number and print.
def reverse_num(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    print("Reversed number:", reversed_num)
num = int(input("Enter a number: "))
reverse_num(num)



#10. Write a program to find if the given number is palindrom or not.
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")
n = int(input("Enter a number: "))
is_palindrome(n)