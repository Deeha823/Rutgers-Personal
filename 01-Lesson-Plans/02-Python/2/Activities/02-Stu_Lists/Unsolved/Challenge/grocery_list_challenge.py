# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries
from multiprocessing.pool import ApplyResult
from ntpath import join
from numpy import append


print("my groceries list")
groceries = ["water", "butter", "eggs", "apples", "sugar", "milk", "cinnonman"]
print(groceries)
print(len(groceries))


# @TODO: Find the first two items on the list
print(groceries[0:2])

# @TODO: Find the last five items on the list
print(groceries[2:])

# @TODO: Find every other item on the list, starting from the second item
print(groceries[1::2])


# @TODO: Add an element to the end of the list
groceries.append("flour")
print(groceries)

# @TODO: Changes a specified element within the list at the given index
groceries.insert(0,"flour")
print(groceries)

# @TODO: Calculate how many items you have in the list
print(len(groceries))

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
print(groceries.index("apples"))
print('Art' in groceries)

for items in groceries:
    print(items)

for index, groceries in enumerate(groceries):
    print(index, groceries)

groceries_str = ', '.join(groceries)
print(groceries_str)

# @TODO: Remove an element from the list based on the given element name
print("Picked up some sugar!")
groceries.remove("milk")
print(groceries)
print()

# @TODO: Remove an element from the list based on the given index






# @TODO: Remove the last element of the list





print("You continue on your journey purchasing groceries...")
