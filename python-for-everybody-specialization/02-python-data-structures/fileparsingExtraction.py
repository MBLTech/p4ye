"""
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
"""

fname = input("Enter Your File Name: ")
fh = open(fname)
count = 0
total = 0
# desiredText = text.find("X-DSPAM-Confidence")
# print(desiredText)
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        # print(line)
        num = line.find(": ")
        # print(num)
        rnums = line[num + 1 :]
        fnums = float(rnums)
        total = total + fnums
        # print(fnums)
        # print(total)

print("Average spam confidence:", total / count)
