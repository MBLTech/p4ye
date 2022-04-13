"""
Lists
"""
# Strings are immutable while lists are mutable
# Lists can consist of integers or strings or both
# Lists can have nested list inside but that list will be considered a single member of the parent list

# myList = [3, "dog", 4, 5, "cat"]
# myList[3] = 10  # list are mutable
# print(myList)
# print(list(myList))  # range usually refers to as elements inside list

"""
Lists Manipulation
"""

# slicing of lists possbile
# lists can be concatenated
# list can be used for large number of inputs summation

# numlist = list()
# while True:
#     try:
#         num = input("Enter a Number: ")
#         num = int(num)
#     except:
#         print("Invalid Argument. Goodbye.")
#         quit()
#     if num == "done":
#         break
#     numlist.append(num)
# print(numlist)

"""
Lists and Strings
"""

# strings split into lists

# some = "My name is Someone"
# print(some.split())
# str1 = "Your:Name:Your:Country"
# print(str1.split()) # Bydefault split() uses spaces for splitting, multiple spaces count as one
# print(str1.split(":"))  # splitting based on colon
