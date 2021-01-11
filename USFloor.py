'''
A Simple silly scrip to convert Europian Floor Number into USfloor number
'''

floor = input('Enter Europian Floor number: ')

#made fail proof for inputs other than integers
try:
    USfloor = int(floor) + 1
except:
    print('Enter the valid Number')
    quit()
print('US Floor number:', USfloor)
