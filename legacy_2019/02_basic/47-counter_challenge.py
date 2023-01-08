list_a = [*range(10,1,-1)]

for i, j in enumerate(list_a):
    print(i, j)

# other solution
for i, j in enumerate(range(10,1,-1)):
    print(i, j)