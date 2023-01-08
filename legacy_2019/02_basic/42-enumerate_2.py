list_a = [
    ['Edu','João','Luiz'],
    ['Maria','Aline','Joana'],
    ['Helena','Ed','Lu'],
]

print(list_a[2][1])

enumer = enumerate(list_a)
print(enumer) # this is an object

# you can (and should) use and enumerated object with a FOR loop
# but it's also possible to convert it into a list

print(list(enumer))

# showing the list
for v1, v2 in enumerate(list_a, 53): # index enumerating starts on 53
    print(v1, v2)

# the same implementation would be
for v1 in enumerate(list_a, 53):
    index_value, the_list = v1
    print(the_list)

# list unpacking on enumerate
for v1 in enumerate(list_a, 53):
    index_value, the_list = v1
    name1, name2, name3 = the_list
    print(name1, name3)