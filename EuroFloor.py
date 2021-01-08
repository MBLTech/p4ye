floor = input('Enter US Floor Number: ')
try:
    Eurofloor = int(floor) - 1
except:
    print('Invalid Entry')
    quit() 
print('Europian Floor Number:', Eurofloor)
