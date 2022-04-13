"""
Python Dictionaries
"""
#
# They are a collection variables
# bag of things in which everything is labled with keyvalue pair, unlike lists which makes them unique
# dict are mutable too
# list has index which tell position while dict has labels for its values(keyvalue pair)
# dict literals (constants) use curly braces and key:value pairs

# Simple dict
#
# myDict = dict()
# myDict["firstitem"] = 9
# myDict["seconditem"] = "Apple"
# print(myDict)
# print(myDict["seconditem"])
# myDict["seconditem"] = "Jelly"  # dict are mutable
# print(myDict)

# counting the number of occurrences in dict
#
# counts = dict()
# names = ["fred", "garry", "tom", "fred", "fred", "tom"]
# # for name in names:
# #     counts[name] = counts.get(name, 0) + 1
# # print(counts)
# #
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)

stuff = dict()
print(stuff.get("candy", -1))
