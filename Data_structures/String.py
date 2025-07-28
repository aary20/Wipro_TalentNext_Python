"""Write a program to count the number of upper and lower case letters in a string."""
str = "Hello World"
high = low = 0
for char in str:
    if char.isupper():
        high += 1
    elif char.islower():
        low += 1
print(f"Upper case letters: {high}, Lower case letters: {low}")


"""Write a program that will checck whether a given string is palindrome or not."""
def is_palindrome(str):
    start = 0
    end = len(str)-1
    while start < end:
        if str[start] != str[end]:
            return False
        start += 1
        end += 1
    return True  
str = input("")
res = is_palindrome(str)
print(f"The given string is a palindrome: {res}")


"""Given a string, return a new string made of n copies of the first 2
chars of the original string where n is the length of the string. The 
string length will be >=2. If the input is Wipro then output sholud be
WiWiWiWiWi."""
srt = input()
n = len(str)  
print(str[0:2]*n)  


"""Given a string , if the first or last character is 'x' , return 
the string without those 'x' character, else return the string unchanged.
If the input is "xHix" ,then output is "Hi" """
str = input()
if str[0]=='x' and str[-1]=='x':
    print(str[1:-1])
else:
    print(str)
    
    
"""Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
You may assume that n is between 0 and the length of the string inclusive. 
For example if the inputs are “Wipro” and 3, then the output should be “propropro”."""
def last_char_repetition(str, n):
    if n > len(str):
        return ""
    return str[-n:] * n
str = input("Enter a string: ")
n = int(input("Enter an integer: "))
result = last_char_repetition(str, n)
print(result)