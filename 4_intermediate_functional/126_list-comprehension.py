# create lists quickly from iterables

# "common" way for other languages
list_a = []
for i in range(10):
    list_a.append(i)
print(list_a)

# repeat a value in the list
list_b = [1 for i in range(10)]
print(list_b)

# iterate
list_c = [i for i in range(10)]
print(list_c) # the same as example a

list_d = [
    i * 2
    for i in range(10)
]
print(list_d)
