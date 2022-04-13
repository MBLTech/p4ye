"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
"""

# Method: 1 (Not working)
#
# fname = input("Enter Your File Name: ")
# fhandle = open("romeo.txt")
# lst = list()
# finalList = 0
# for line in fhandle:
# print(line.rstrip())
# flst = line.split()
# finalList = flst
# print(flst)
# print(finalList)

# Mehtod: 2

fname = input("Enter Your File Name: ")
fhandle = open(fname)
fr = fhandle.read()
fl = fr.split()
# print(fl)
flr = sorted(fl)
fd = list()
for i in flr:  # Removing duplicates from the list
    if i not in fd:
        fd.append(i)
print(str(fd))
