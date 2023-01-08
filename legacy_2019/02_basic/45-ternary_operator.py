logged_user = False

# normal
if logged_user:
    msg = 'User logged'
else:
    msg = 'User must log in'
print(msg)

# ternary operator
msg = 'User logged' if logged_user else 'User must log in'
print(msg)

# another example
age = input("What's your age? ")

if not age.isnumeric():
    print('You must type only numbers')
else:
    msg = 'Can access' if int(age) >= 18 else 'Cannot access'
    print(msg)