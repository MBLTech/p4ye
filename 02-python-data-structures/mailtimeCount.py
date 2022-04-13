"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hrsCount = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        timeRange = line[5]
        # print(timeRange)
        timerangeList = timeRange.split(":")
        actualhrs = timerangeList[0].split()
        # print(actualhrs)
        for hrs in actualhrs:
            hrsCount[hrs] = hrsCount.get(hrs, 0) + 1
print(hrsCount)
tmp = sorted(hrsCount.items())
for hrs, freq in tmp:
    print(hrs, freq)

# Redundant part, not needed for exercise
# Reversing Key:Value pair via tuples
# rhrsCount = []
# for k, v in hrsCount.items():
#     rhrsCount.append((v, k))
# tmp = sorted(rhrsCount)
# print(tmp)
