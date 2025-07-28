"""Write a program to print the 4th element from first and 4th element from last in a tuple."""
tup = (10, 20, 30, 40, 50, 60, 70, 80)
if len(tup) > 4:
    b = int(input("Enter the place or element:"))
    print(tup[b-1], tup[-b])
else:
    print("The tuple does not have enough elements.")


"""Write a program to check whether an element exists in a tuple or not."""
tup  =(1,2,3,4,5,6,6,7,23,4)
a1 = int(input("Enter the element to check: "))
for i in tup:
    if a1 == i:
        print(f"The number {a1} exists")
        break 
    else:
        print(f"The number {a1} does not exist")


"""Write a program to convert a list into a tuple."""
lst = (1,2,3,4,5,5,3)
lst = tuple(lst)  
print(type(lst))


"""Write a program to find the index of an item in a tuple."""
tup = (1,2,3,4,5,5,3)
a2 = int(input("Enter the number to check: "))
if a2 in tup:
    print(tup.index(a2))


"""Write a program to replace last value of tuples in a list to 100"""
lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
lst1 = []
for i in lst:
    lst1.append(list(i)) 
for i in lst1:
    i[-1] = 100
print(lst1)
