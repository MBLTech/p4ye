firstvalue = input('Enter Your First Number: ')
firstvalue = int(firstvalue)
secondvalue = input('Enter Your Second Number: ')
secondvalue = int(secondvalue)
sum = 0
for i in range (firstvalue,secondvalue):
    sum = sum + i
print('Your Total is: ',sum)
