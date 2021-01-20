sum = 0
count = 0

while True:
    num = input('Input your number: ')
    if num == 'done':
        print('goodbye')
        break
    try:
        fnum = float(num)
    except:
        print('bad input')
        continue
    sum = sum + fnum
    count = count + 1

print('total inputs:', count)
print('Sum:', sum)
print('average:', sum/count)
