'''
     ###############################################
    #    #######################################    #
####    ########   Simple Calculator   ##########    ####
    #   #######################################     #
    ###############################################
'''

# This is very simple calc which only takes two arguments and spit out result
# for four basic numeric operations, and continue to take arguments until your
# with your two digits calc and enter 'done' for either of the input values
while True:
    x = input('Enter 1st Value: ')
    if x == 'done':
        print('Goodbye')
        break
    try:
        xf = float(x)
    except:
        print('Enter Numberics Only')
        continue

    y = input('Enter 2nd Value: ')
    if y == 'done':
        print('Goodbye')
        break
    try:
        yf = float(y)
    except:
        print('Enter Numberics Only')
        continue
    sum = xf + yf
    substraction = xf - yf
    multiple = xf * yf
    division = xf / yf

    print('Summation:', sum)
    print('Substraction:', substraction)
    print('Multiplication:', multiple)
    print('Division', division)
