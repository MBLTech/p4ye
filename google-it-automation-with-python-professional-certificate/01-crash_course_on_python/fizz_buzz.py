# for i in range (1, 101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)
n = 1
while n <=100:
    if n%3 == 0 and n%5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)
    n += 1
