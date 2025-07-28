"""Write a program to create a list of 5 integers and display
the list items.Access individual elements through index. """
lst = [10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])


"""Write a program to append a new item to the end of the list"""
lst = [10,20,30,40]
lst.append(50)
print(lst)  


"""Write a program to reverse the order of the items in the list"""
lst = [50,40,30,20,10]
lst.reverse()
print(lst)  


"""Write a program to print the number of occurrences of a specified element in a list."""
lst = [4,4,4,3,2,4,1,2]
c = int(input())
b = lst.count(c)
print(f"The number of occurrences of {c} is:{b}")


"""Write a program to append the items of list1 to list2 in the front"""
l1 = [4,5,6]
l2 = [1,2,3]
l1 = l1 + l2
print(l1)


"""Write a program to remove the item from a specified index in a list"""
lst = [10,20,30,40,50]
lst.pop(20)
print(lst)  


"""Write a program to insert a new item before the element in an existing list."""
lst = [10,20,30,40,50]
lst.insert(10,20)
print(lst)   


"""Write a program to remove the  first occurrence of  a specified element in a list"""
lst = [1,4,3,4,5,6,4]
occur = int(input())
if occur in lst:
    lst.remove(occur)
print(lst)    