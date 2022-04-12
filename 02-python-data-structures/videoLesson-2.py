"""
Opening a File
"""
# fileHandle = open(
#     "textFile.txt", "r"
# )  # Opening .txt file with read permission or 'w' for write permissions

# File = open("someFile.txt")
# for sometext in File:
#     print("sometext")  # It will print out the text as a string line by line

# Counting lines

# fhandle = open("sample.txt")
# count = 0
# for line in fhandle:
#     count = count + 1
#     print("Line Count:", count)
"""
Reading through the Whole file
"""

# fhandle = open("sample.txt")
# chars = fhandle.read()
# print(len(chars))
# print(chars[300:400])

# for line in fhandle:
#     if not line.startswith("we"):
#         continue
#     print(line)

# for line in fhandle:
#     line = line.rstrip()
#     if not "we" in line:
#         continue
#     print(line)

"""
Prompt for File Names and Bad File Names
"""
fname = input("Please Enter your File Name: ")
try:
    fhand = open(fname)
except:
    print("Not a Valid File: ", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("we"):
        count = count + 1
print("total count", count, "in", fname)
