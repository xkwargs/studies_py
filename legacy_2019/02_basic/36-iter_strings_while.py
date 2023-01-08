# indexes
#           0123456789.......................33
sentence = 'o rato roeu a roupa do rei de roma'
sentence_len = len(sentence)
print(sentence_len) # includes zero and counts ALL positions, so it will be 34

counter = 0
new_string = ''

#while counter < sentence_len:
    # print(sentence[counter], counter)
#    new_string += sentence[counter]
#    print(new_string)
#    counter += 1

user_input = input("Which char would you like to capitalize? ")

while counter < sentence_len:
    char = sentence[counter]
    if char == user_input:
        new_string += user_input.upper()
    else:
        new_string += char
    counter += 1

print(new_string)