user = input('Type your name: ')
char_len = len(user)

if char_len < 6:
    print('You must type at least 6 characters')
else:
    print('Success')

print(
    user, type(user), "\n",
    char_len, type(char_len)
)

# Check the quantity of chars typed

string1 = input('Type something: ')
string2 = input('Type somthing else: ')

print(f'Total was {len(string1) + len(string2)}')

# the function len() just calls the method __len__() from class string on object 'string2'

print(len(string2))
print(string2.__len__())

# objects of type int, float, bool, etc.. cannot have the method len() !!

try:
    print(len(123456))
except Exception as e:
    print(e, '. I told you')