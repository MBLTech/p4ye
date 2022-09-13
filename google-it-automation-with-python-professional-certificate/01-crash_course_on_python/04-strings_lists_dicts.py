# Strings

# Indexing: starts at zero
# name = 'Alice'
# print(name[0])
# print(name[-1])

# def first_and_last(message):
#     if len(message) == 0:
#         return True
#     if message[0] == message[-1]:
#         return True
#     else:
#         return False

# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))

# m = 'A'
# print(m[0])
# print(m[-1])

# String slicing

# name = 'GrapeFruit'
# print(name[:5])
# print(name[5:])

# message = "A silly catt loves to eat bananas"
# # message[11] = ""
# new_message = message[:11] + "" + message[12:]
# print(new_message)

# Method 

# message = "A silly catt loves to eat bananas."

# print(message.index("catt"))
# inmethod = "catt" in message
# print(inmethod)

# print(message.count("A"))
# print(message.endswith("bananas."))
# print(message.isnumeric())
# print(message.split())

# print(" ".join(["This","is","a","grape"]))

# name = "Manny"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))

# print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

# Formating Expression

# price = 7.5
# with_tax = price * 1.09
# print(price, with_tax)

# print("Base price: {:.2f}. With Tax: {:.2f}".format(price, with_tax))

# message = "My name is Bob"
# print(message.split(" "))
# print(message.replace(" ", "|"))


