'''
####################################################################
####################################################################
################### Number Range Summation #########################
####################################################################
####################################################################
'''

while True:
    print ("Type 'done'to Quit.")
    sum = 0
    firstvalue = input('Enter Your First Number: ')
    if firstvalue == 'done' :
        print('Thankyou for using NRS')
        break
    try:
        firstvalueint = int(firstvalue)
    except:
        print('Enter Integers Only')
        continue
    secondvalue = input('Enter Your Second Number: ')
    if secondvalue == 'done':
        print('Thankyou for using NRS')
    try:
        secondvalueint = int(secondvalue)
    except:
        print('Enter Intergers Only')
        continue
    for i in range (firstvalueint,secondvalueint):
        sum = sum + i
    print('Your Total is: ',sum)
