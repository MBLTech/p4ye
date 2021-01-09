'''
 This program will take multiple inputs from the user and when he enters done
 as his last input it will return largest and smallest values of user's
 respective inputs
'''

#we are using none as in the loop first value will replace them automatically
largest = None
smallest = None

while True:
    num = input('Input Number: ')

#breaking program here will not mess up placeholders(would be replaced with
# invalid input and whole program would throw an error.(try yourself))
    if num == 'done':
        break
    try:
        fnum = float(num)
#putting 'continue' will reset the loop and it'll again ask for input(handy for
# taking multiple inputs from the user)
    except:
        print('Invalid input')
        continue
    if largest == None or fnum > largest:
        largest = fnum


    if smallest == None or fnum < smallest:
        smallest = fnum

print('The largest value is', largest)
print('The smallest value is', smallest)
