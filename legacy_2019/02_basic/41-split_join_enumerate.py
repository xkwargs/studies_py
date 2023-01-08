"""
Split, Join, Enumerate in Python

* Split - Divide a String # str
* Join - Join a list # str
* Enumerate - Enumerate elements from list # iterables
"""

string = "Brazil is the country of football, Brazil is five-time champion."
list_a = string.split(' ')
list_b = string.split(',')

print(list_a)
print(list_b)

word = ''
count_word = 0

for v in list_a:
    # print(f"The word {v} appeared {list_a.count(v)}x in the statement.")
    repetitions = list_a.count(v)

    if repetitions > count_word:
        count_word = repetitions
        word = v

print(f"The word with more repetitions was {word} ({count_word}x)")

for v in list_b:
    print(v.strip().upper())

string = 'O Brasil é penta'
list_c = string.split(' ')
print(list_c)

string_b = ','.join(list_c)
print(string_b)

# unpacking elements

for id, value in enumerate(list_c):
    print(id, value, list_c[id]) # unpacking with 'value' and referencing 'list[i]' is the same

list_d = [
    [1,'Jônatas'],
    [3,'Dayane'],
    [5,'Rebeca']
]
for v in list_d:
    print(v[0], v[1]) # picks each value, normally.. follows the logic

for index, name in list_d:
    print(index, name)

# which has the same behavior of

list_e = ['Jônatas', 'Dayane', 'Rebeca']

for index, name in enumerate(list_e):
    print(index, name)

# list unpacking

n1, n2, n3 = list_e
print(n2)