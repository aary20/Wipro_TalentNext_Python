import count_vowels
import frequency_letter
import is_palindrome

name = input("Enter a string: ")
print("The string is plaindrome:",is_palindrome.is_palindrome(name))
print("The number of vowels in string:",count_vowels.count_the_vowels(name))
print("Frequency of letters:",frequency_letter.frequency(name))