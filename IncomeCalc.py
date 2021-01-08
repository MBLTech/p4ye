hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print('Invalid Formate')
    quit()

if h > 40:
    otphrs = h - 40
    print('Overtime=', otphrs, 'hrs')
    print('Overtime Rate=', r * 1.5)
    overtime = (h - 40.0) * (r * 1.5)
    pay = 40 * r
    print('Net pay:', pay + overtime)
else:
    print('Regular')
    reg = h * r
    print('Net Pay:', reg)
