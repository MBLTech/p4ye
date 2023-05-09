# Boolean Operator has 2 values, True, or False
# Conditional Statements
#
# print('Ask for The Name: ')
# name = input()
# if name == 'Alice':
#     print('Hi, Alice.')


# print('Enter a name, ')
# name = input()
# # if name != '':
# #     print('Thank you for entering a name.')
# # else:
# #     print('You did not enter a name.')


# When there is empty input string the condition is False, otherwise it is True. A Truthy or Falsey value
#
# if name:
#     print('Thank you for entering a name.')
# else:
#     print('You did not enter a name.')


# To check wether a value is Truthy or Falsey
#
# print(bool(0))
# print(bool(0.0))
# print(bool(''))
# print(bool(42.0))


# While loops: break statement
#
# print('Enter your name: ')
# name = input()
# while True:
#     if name == ''  or len(name) <= 2:
#         print('You did not type your correct name. Try Again!')
#         break
#     print('Thank you, ' + name)
#     break


# While loops: continue statement
#
# spam = 0
# while spam < 10:
#     spam += 1
#     if spam == 4:
#         continue
#     print('spam is ' + str(spam))


# For loops
#
# print('My name is')
# for i in range(5):
#     print('Bob Five Times ' + str(i))

# total = 0 # Get the sum of numbers upto 100
# for i in range (101):
#     total += i
# print('Sum: ' + str(total))

# for i in range (0, 100, 2): # Range function can have three values
#     print(i)