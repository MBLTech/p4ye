"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
mailcount = dict()
mail = None
mailMax = None
for line in handle:
    if line.startswith("From "):
        line = line.split()
        mailaddr = line[1]
        mailaddr = mailaddr.split()
        for mail in mailaddr:
            mailcount[mail] = mailcount.get(mail, 0) + 1
# print(mailcount)
for person, count in mailcount.items():
    if mailMax is None or count > mailMax:
        mail = person
        mailMax = count
print(mail, mailMax)
