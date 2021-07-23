'''
A Simple silly script to convert USfloor number into Europian floor number
'''

floor = input('Enter US Floor Number: ')

#made fail proof for inputs other than integers
try:
    Eurofloor = int(floor) - 1
except:
    print('Invalid Entry')
    quit()
print('Europian Floor Number:', Eurofloor)
