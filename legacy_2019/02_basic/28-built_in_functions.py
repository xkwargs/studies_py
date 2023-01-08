# https://docs.python.org/3/library/stdtypes.html#str.isdecimal

num1 = input('Type number 1: ')
num2 = input('Type number 2: ')

# isnumeric isdigit isdecimal
# will check only numbers, and positives. no negatives/floats will be verified

print(num1.isnumeric())
print(num2.isnumeric())

# alternative solution

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True

# False
print(is_number('123a'))  # False

# test from previous example

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('Wrong input')

# check later... isalnum()