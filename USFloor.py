floor = input('Enter Europian Floor number: ')
try:
    USfloor = int(floor) + 1
except:
    print('Enter the valid Number')
    quit()
print('US Floor number:', USfloor)
