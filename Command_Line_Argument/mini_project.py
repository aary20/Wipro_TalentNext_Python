"""Through command line arguments three strings seperated by space are given to you.
Each string is a series of numbers seperated by hyphen(-). You like allnumbers in string 1 and dislike all
numbers in string 2.

Third string contains the numbers given to you. Your initial happiness is 0.
When you encounter a number which is present in string 1,add 1 to your happiness, if it is present in string 2,
add -1 to your happiness. Otherwise  your happiness does not change.
Output your final happiness at the end."""

import sys

def count_happiness(likes_str, dislikes_str, items_str):
    likes = list(map(int, likes_str.split("-")))
    dislikes = list(map(int, dislikes_str.split("-")))
    items = list(map(int, items_str.split("-")))

    happiness = 0

    for item in items:
        if item in likes:
            happiness += 1
        elif item in dislikes:
            happiness -= 1

    return happiness

likes_input = sys.argv[1]
dislikes_input = sys.argv[2]
items_input = sys.argv[3]

score = count_happiness(likes_input, dislikes_input, items_input)
print("Happiness Score:", score)