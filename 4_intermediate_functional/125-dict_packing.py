# Dict Packing Unpacking
a, b = 1, 2
a, b = b, a
# print(a, b)

person = {
    'name': 'Aline',
    'last_name': 'Souza'
}

person_data = {
    'age': 16,
    'height': 1.6
}

# unpacking using items()
a, b = person.items()
print(a, b)

# internally unpacking using items()
(a1, a2), (b1, b2) = person.items()
print(a1, a2)
print(b1, b2)

# same using for statement
for k, v in person.items():
    print(k, v)

# extract one dict inside another one (merge data)
person_complete = {**person, **person_data}
print(person_complete)

# args and kwargs
def show_named_args(*args, **kwargs):
    print('NOT NAMED: ', args)
    print('NAMED: ', kwargs)

show_named_args(1, 2, name='Joana', aaa=123) # and keep them packed
show_named_args(**person_complete) # or unpack them