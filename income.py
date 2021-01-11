'''
A simple exercie sript to find out total pay by multiplying hours worked with
rate per hour.
'''

hr1 = input('Enter Hours: ')
rate1 = input('Enter Rate: ')

# made failure proof so if user inputs values other than number it won't crash
# and through an error. so the program will just quit with following warning
# to the user
try:
    hrs = float(hr1)
    rate = float(rate1)

# scrip can be made much better by adding 'continue' instead of 'quit()' in a
# while loop so that by printing failure message it just asks user for other
# input instead of quiting
except:
    print('Failure: Enter Integers Only')
    quit()

pay = float(hrs * rate)

print('Pay:', pay)
