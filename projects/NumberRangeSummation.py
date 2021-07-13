'''
####################################################################
####################################################################
################### Number Range Summation #########################
####################################################################
####################################################################
'''

while True:
    sum = 0
    firstvalue = input('Enter Your First Number: ')
    if firstvalue == 'quit' :
        print('Thankyou for using NRS')
        break
    try:
        firstvalueint = int(firstvalue)
    except:
        print('Enter Integers Only')
        continue
    secondvalue = input('Enter Your Second Number: ')
    if secondvalue == 'quit':
        print('Thankyou for using NRS')
    try:
        secondvalueint = int(secondvalue)
    except:
        print('Enter Intergers Only')
        continue
    for i in range (firstvalueint,secondvalueint):
        sum = sum + i
    print('Your Total is: ',sum)
