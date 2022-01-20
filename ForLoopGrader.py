'''
To know the largest number in the given for loop
'''

largest = None # largest has no value

for n in (88, 33, 32, 55, 9, 77, 55, 10, 11, 33, 55, 99, 101, 77, 6, 66, 33):
    if largest is None :
        largest = n #largest will get the first value from n number range
    elif largest < n : # If n is larger than the value of 'largest', loop will run and smallest will attain the value of n
        largest = n
        print("The Largest so far:", largest)
print("The Largest Number is:", largest)

'''
To evaluate the smallest number from a for loop
'''

smallest = None # smallest has no value

for n in (88, 33, 32, 55, 9, 77, 55, 10, 11, 33, 55, 99, 101, 77, 6, 66, 33):
    if smallest is None :
        smallest = n #smallest will get the first value from n number range
    elif smallest > n : # If n is less than the value of 'smallest', loop will run and smallest will attain the value of n
        smallest = n
        print("The Smallest so far:", smallest)
print("The Smallest Number is:", smallest)