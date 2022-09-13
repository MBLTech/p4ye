'''
A simple exercise program which calculates the total income by taking input of
of hours worked and rate per hour. But it is little different from program
'income.py' as it also calculates overtime with rate 1.5 times of the normal
per rate.
'''

hrs = input("Enter Hours:")
rate = input("Enter Rate:")

# made failure proof using try except statements to allow user only enter
# numbers(integers/float) otherwise through an error
try:
    h = float(hrs)
    r = float(rate)
except:
    print('Invalid Formate')
    quit()

# this script calculates overtime by taking standard 40 hours per week work
# and rest working hours as overtime and handles them with 1.5 times the normal
# per hour rate.

if h > 40:
    otphrs = h - 40
    print('Overtime=', otphrs, 'hrs')
    print('Overtime Rate=', r * 1.5)
    overtime = (h - 40.0) * (r * 1.5)
    pay = 40 * r
    print('Net pay:', pay + overtime)
#In case hours are less than 40 hours it will calculate the pay as regular with
# provided per hour rate.
else:
    print('Regular')
    reg = h * r
    print('Net Pay:', reg)
