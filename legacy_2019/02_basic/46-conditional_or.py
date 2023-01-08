name = input("What's your name? ")

# default
if name:
    print(name)
else:
    print("You haven't typed anything")

# pythonish
print(name or "You haven't typed anything")

# if you have multiple conditions, it will stop in the first true
print(name or None or False or 0 or "You haven't typed anything" or "Other")
# string is true by default

# other example
a = 0
b = None
c = False
d = []
e = {}
f = 22 # the first 'true' value
g = 'Luiz'

var = a or b or c or d or e or f or g
print(var)
