# Conditionals
#
# def hint_username(username):
#     if len(username) <= 3:
#         print("Invalid username. Must be at least 3 characters long")
#     else:
#         return username


# name_prompt = input("Choose Your username: ")

# if True:
#     validity_username = hint_username(name_prompt)
#     if validity_username != None:
#         print("Welcome " + str(validity_username) + " to the Department")
#
# Loops
# While Loops
# def attempts(n):
#     x = 1
#     while x <= n:
#         print("Attemp " + str(x))
#         x += 1
#     print("Done")
# attempts(5)

# x = 1
# sum = 0
# while x < 10:
#     sum += x
#     x += 1
#
# x = 1
# product = 1
# while x < 10:
#     product *= x
#     x += 1
#     print(product, x)
# print(product, x)

# Infinite Loops

# For Loops

# for x in range (0, 100, 2):
#     print(x)

# friends = ['Alex', 'Bob', 'Alice']
# for friend in friends:
#     print("Hi", friend)

# sentence = "My name is Alex"
# for letter in sentence:
#     print(letter)

# Nested For Loops

# for left in range(7):
#     for right in range(left, 7):
#         print("[" + str(left) + "|" + str(right) + "]", end=" ")
#     print()

# teams = ["Dragon", "Wolves", "Pandas", "Unicorn"]
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + " vs " + away_team)

# Recursion

"""
The repeated application of the same procedure to a smaller problem.

or

Recursion lets us tackle complex problems by reducing the problem to a simpler one.
"""
# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n-1)

# print(factorial(6))

# def sum_numbers(n):
#     if n < 1:
#         return 0
#     return n + sum_numbers(n-1)

# print(sum_numbers(5))
# print(sum_numbers(10))


