'''
Its the 2nd version of Incomecalc.py and made using function statement
there is nothing new, just the same program with function defined.
'''

try:
    hrs = float(input('Enter Hours:'))
    rph = float(input('Enter Rate Per Hour:'))
except:
    print('Invalid Format')
    quit()

# The function to calculate total pay in case of normal as well as when extra hours are served.
def computepay():
    if hrs <= 40:
        netpay= hrs * rph # Calculating the net pay if there are no extra hours worked
        return netpay
    else:
        otp = (hrs - 40) * 1.5 * rph + (40 * rph) # The net pay when being worked more than 40 hours calculating overtime with rate of 1.5 times of the original rate per hour, and the rest of 40 hours will be calculated as the normal rate per hour of the persion getting payment.
        return otp
print("Pay", computepay())