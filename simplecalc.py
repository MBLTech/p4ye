'''
     ###############################################
    #    #######################################    #
####    ########   Simple Calculator   ##########     ####
    #   #######################################     #
    ###############################################
'''

while True:
    x = input('Enter 1st Value: ')
    y = input('Enter 2nd Value: ')
    if x == 'done' or y == 'done':
        print('Goodbye')
        break
    try:
        xf = float(x)
        yf = float(y)
    except:
        print('Enter Numberics Only')
        continue
    sum = xf + yf
    print('Total:', sum)
