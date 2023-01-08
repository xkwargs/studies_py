text = 'Python'

# the complex 'while' way
c = 0
while c < len(text):
    print(text[c])
    c += 1

print()

# the more semantic 'for'
for char in text:
    print(char)

for n, char in enumerate(text):
    print(n, char)

print(enumerate(text))

# function range(start=0, stop, step=1)

for n in range(10):
    print(n)

for n in range(10,2,-2):
    print(n)

# find the multiple by 8
for n in range(100):
    if n % 8 == 0:
        print(n)

print('##########')

# which is the same as
for n in range(1,100,8):
    print(n)

# iterating over a string

new_string = ''
for char in text:
    if char == 't' or char == 'h':
        new_string += char.upper()
    elif char == 'y':
        continue # jumps to the next loop and doesn't enter 'else'
    elif char == 'o':
        break # just finishes the loop
    else:
        new_string += char

print(new_string)