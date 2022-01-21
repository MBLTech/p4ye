"""
A Simple silly script to convert USfloor number into European floor number
"""

floor = input("Enter US Floor Number: ")

# made fail proof for inputs other than integers
try:
    Eurofloor = int(floor) - 1
except:
    print("Invalid Entry")
    quit()
print("European Floor Number:", Eurofloor)
