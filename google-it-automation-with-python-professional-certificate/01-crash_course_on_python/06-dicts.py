# Dictionary
'''
The data inside dictionaries take the form of pairs of keys and values.
'''

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 20
del file_counts["py"] # del keyword followed by key in square brackets to delete the value inside dict
print(file_counts)
print(type(file_counts)) # type() method to check data type
valid_ele = "jpg" in file_counts # in key word to check if a key is contained in a dictionary
print(valid_ele)

# Iterating over the contents of a Dictionary

for ext in file_counts:
    print(ext) # Iteration variable will go through the keys in dict, for for loop.

for ext, amount in file_counts.items(): # items() method can be used to access the both key, value pairs in the dict inside the loop
    print("There are {} files of type {}".format(amount, ext))

file_counts.keys() # Just access the dict keys
file_counts.values() # Just access the values of the dict

# Make a func which prints a dictionary with total number of letter as a value, and the letter itself as a key.

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aabbcc"))
print(file_counts.get("cfg"))
