"""
    Formatando valores com modificadores

    :s - Texto (strings)
    :d - Inteiros (int)
    :f - Números de ponto flutuante (float)
    :.[number]f - Quantidade de casas decimais (float) ex  :.2f
    :[char][> ou < ou ^][qty][type - s, d, f]

    > - Esquerda
    < - Direita
    ^ - Centro
"""

num_1 = 10
num_2 = 3
div = num_1 / num_2

print( '{:.2f}'.format(div) )
print( f'{div:.2f}' )

name = 'Jônatas'
print(f'{name:s}')

print(f'{num_2:0>10}')
print(f'{1150:0>10}')
print(f'{9999:0^10}')
print(f'{9999:0^10.2f}')

print(f'{name:#^50}')
print((50-len(name)) / 2)

formatted_name = '{:@>50}'.format(name)
print(formatted_name)
formatted_name = '{:@>5}'.format(name)
print(formatted_name)

formatted_name = '{n:0<20}'.format(n=name)
print(formatted_name)

middle_name = 'Rosa da Silva'
last_name = 'Bonventi'

formatted_name = '{0:$^11}{1:#^19}'.format(name, middle_name, last_name)
print(formatted_name)

print(name.zfill(20))
print(name.ljust(20, '#'))

name = 'jônataS'
print(name.lower()) # all lower case
print(name.upper()) # all upper case
print(name.title()) # first letters capitalized