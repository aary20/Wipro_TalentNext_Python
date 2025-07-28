"""Write a program to add a key and value to a dictionary."""
dict = {Name:"Aarya", Age:20}
print(dict)
dict["City"] = "Bhopal"
print(dict)   

"""Write a program to concatenate the following dictionaries to create a new one"""
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}

result = {**dict1, **dict2, **dict3}
print(result)


"""Write a program to check if a given key already exists in a dictionary. """
dict = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

k = int(input("Enter a key to check: "))

if k in dict:
    print(f"The key {k} is present.")
else:
    print(f"The key {k} is not present.")


""" Write a program to iterate over a dictionary using for loop """
dict = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

print("Keys:", *dict)

print("Values:", *dict.values())

print("Key-Value Pairs:")
for key, value in dict.items():
    print(f"{key}: {value}")


"""Write a program to prepare a dictionary where the keys are numbers between
1 and 15 (both included) and the values are square of the keys."""
dict = {}
for i in range(1, 16):
    square = i * i
    dict[i] = square

print(dict)


"""Write a program to sum all the values in a dictionary,
considering the values will be of int type."""
dict={'a':1,'b':2,'c':3,'d':4}
sum1=0
for i in dict:
    sum1=sum1+dict[i]
print(sum1)