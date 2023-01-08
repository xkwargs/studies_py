# traditional
x = 10
y = 'Luiz'

z = x
x = y
y = z
print(f'x={x}, y={y}')

# 'pythonish'
x = 10
y = 'Luiz'

x,y = y,x
print(f'x={x}, y={y}')

# you can go complex
x = 10
y = 'Rebeca'
z = 'Jônatas'

print()
print(f'x={x}, y={y}, z={z}')
x,y,z = z,x,y
print(f'x={x}, y={y}, z={z}')