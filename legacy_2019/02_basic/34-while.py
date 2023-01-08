x = 0

while x < 5:
    print(x)
    x = x + 1

print("It's over!")

# conditions that may cause errors

x = 0
while x < 10:
    if x == 3:
        x = x + 1 # this will just skip printing 3, since we don't have a print before going to the next loop
        #print(x) # will keep printing 3 eternally, if line above is commented
        continue # will go to the next loop

    print(x)
    x = x+1

print("It's over!")

# fake rows and columns

x = 0 # column
y = 0 # row

while x < 10:
    y = 0 # row
    while y < 5:
        print(f'X = {x}, Y = {y}')
        y += 1
    x += 1

print('Done')