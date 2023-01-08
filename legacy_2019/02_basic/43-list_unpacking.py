list_a = ['Luiz', 'João', 'Maria']

n1, n2, n3 = list_a # variables must match the quantity of indexes in the list
print(n2)

# another way to solve it
n1, n2, *other_list = list_a
print(n1, n2)
print(n1, n2, other_list)

list_b = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

# get n first and n last positions
n1, n2, n3, *other_list, last_value = list_b
print(other_list)

# convention to say the rest of list won't be used
n1, n2, *_ = list_b
print(n1, n2)