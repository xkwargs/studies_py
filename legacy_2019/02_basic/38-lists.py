# lists

#           0 1 2   3    4
list_one = [1,2,3,'Hey',True]
print(list_one[3])

list_one[3] = 'Ho'
print(list_one[3])

print(list_one[0:3]) # get a range (will return a list)
print(list_one[-1]) # get the last element
print(list_one[::2]) # all elements, step=2
print(list_one[::-1]) # step=backwards(?)

# concatenate lists
l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
print(l3)
l1.extend(l2) # will override l1
l1.extend('a') # also one way to add a single element
print(l1)

# adding elements to the list
l2.append('b') # new index added too
print(l2)

l2.insert(0, 'banana') # same but you can specify an index
print(l2)

# deleting elements from the list
l2.pop() # will delete the last element
print(l2)

# generating list
l2 = []
for i in range(1,10):
    l2.append(i)
print(l2)

l2 = list(range(1,100,8))
print(l2)

# deleting a single index, or slice (from index)
del(l2[3:5])
print(l2)

# adding up all values
l2 = [0,1,2,3,4,5,6,7,8,9]

sum = 0
for v in l2:
    sum = sum + v

print(sum)

# identifying element types in a list
l2 = ['String', True, -10, -20.5]

for elem in l2:
    print(f'The type is {type(elem)} and the value is {elem}')

# small game of guessing secret word
secret = 'python'
typed = []
attempts = 3

while True:
    if attempts <= 0:
        print('You lost :/')
        break

    char = input('Type a letter: ')

    if len(char) > 1:
        print('No cheating! You can only type one letter at once.')
        continue # will go to the next loop, without entering the next statement

    typed.append(char)

    if char in secret:
        print(f'Nice! Letter "{char}" exists in the secret word.')
    else:
        print(f"Ouch! Letter {char} doesn't exist.")
        typed.pop() # important part is here

    secret_temp = ''
    for secret_char in secret: # will run the entire sentence
        if secret_char in typed:
            secret_temp += secret_char # if matches, fill with the char
        else:
            secret_temp += '*' # if not, fill with an *

    if secret_temp == secret:
        print(f'You won! :) The word is {secret_temp}')
        break
    else:
        if char not in secret:
            attempts -= 1
        print(f'The word is currently {secret_temp}. You have {attempts} attempts left.')
