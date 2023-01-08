list_one = ['Jônatas Rosa', 'Teste', 'Nome']

for v in list_one:
    print(v)
    continue # always will go to the next loop
    print(v) # won't execute

for v in list_one:
    print(v) # this will only execute one time
    break
    # will interrupt the loop
    print(v) # won't execute

# regular IF / ELSE statement

starts_with_j = False
for v in list_one:
    if v.lower().startswith('j'):
        print('Starts with J:', v)
        starts_with_j = True

if starts_with_j:
    print("There is one word starting with J")
else:
    print("There is no word starting with J")

# using FOR / ELSE

for v in list_one:
    print(v)
    if v.lower().startswith('j'):
        break
else:
    print("There is no word starting with J")