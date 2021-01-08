hr1 = input('Enter Hours: ')
rate1 = input('Enter Rate: ')

try:
    hrs = float(hr1)
    rate = float(rate1)
except:
    print('Failure: Enter Integers Only')
    quit()

pay = float(hrs * rate)

print('Pay:', pay)
