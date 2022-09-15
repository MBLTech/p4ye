# Lists

# Modifying Lists

# fruits = ["Apple", "Banana", "Grape"]
# fruits.append("Mango")
# print(fruits)

# fruits.insert(0, "Orange")
# fruits.insert(-1, "Avacado")
# print(fruits)

# Lists and Tuples
# tuple = ("Top Secret", "docx", 34)
# print(tuple)
# missionName, docType, code = tuple # Unpacking of tuples
# print(code)

# Iterating over lists and Tuples
'''
Enumerate methods has two variables, index and elememnt of the list.
'''
# winners = ["David", "John", "Reese"]
# # for index, person in enumerate(winners):
# #     print("{} - {}".format(index + 1, person))
# for index, name in enumerate(winners):
#     print(index, " | ", name)

# List Comprehensions
'''
Lets us create new lists based on sequences or range
'''

# Without list Comprehensions

# multiples = []
# for x in range (1, 11):
#     multiples.append(x*7)
# print(multiples)

# With list Comprehensions

# multiples_comp = [x*7 for x in range (1, 11)] 
# print(multiples_comp)

# langs = ["Python", "JS", "Golang", "Rust"]
# lens = [len(lang) for lang in langs]
# print(lens)
