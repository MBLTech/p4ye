largest = None
smallest = None
#how to resolve assigning both values to one var
while True:
    num = input('Enter a Number: ')
    try:
        value = float(num)
        if value == 'done':
            break
    except:
        print('Invlaid input')
        continue

        if largest is None and smallest is None:
            value = None
            print(value)
            i m working on it
