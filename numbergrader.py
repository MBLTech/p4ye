largest = 0
smallest = 0

while True:
    num = input('Input Number: ')
    if num == 'done':
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    if largest == 0 or fnum >= largest:
        largest = fnum
    else:
        largest = largest

    if smallest == 0 or fnum <= smallest:
        smallest = fnum
    else:
        smallest = smallest
print('The largest value is', largest)
print('The smallest value is', smallest)
