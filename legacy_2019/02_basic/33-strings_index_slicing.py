text = 'Python s2'

#              Python s2
# positives   [012345678]
# negatives - [987654321]

print(text[2])
print(text[len(text)-2])
print(text[-2])

url = 'www.google.com/'
print(url[:-1])

# creating new strings with slicing

new_string = text[2:6]
print(new_string)
print(text[0:6])
print(text[7:])
print(text[-9])
print(text[-9:-3])
print(text[0::2]) # start|end(all)|step
print(text[0:6:2]) # other example

# check later... built-in functions