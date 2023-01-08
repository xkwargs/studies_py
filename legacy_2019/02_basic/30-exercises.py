"""
    Faça um programa que peça ao usuário para digitar um número inteiro, e informe se este número é par um ímpar. Caso o
    usuário não digite um número inteiro, informe que não é um número inteiro.
"""

int_value = input('Type an int value: ')

if int_value.isdigit():
    int_value = int(int_value)

    if int_value % 2 == 0:
        print(f'{int_value} is even')
    else:
        print(f'{int_value} is odd')
else:
    print('This is not an int number')

"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
    Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

time = input('Type a time (0-23): ')

if time.isdigit():
    time = int(time)

    if time < 0 and time > 23:
        print('Time must be between 0 and 23')
    else:
        if time <= 11:
            print('Good morning!')
        elif time <= 17:
            print('Good afternoon!')
        else:
            print('Good night!')
else:
    print('Please type a valid hour between 0 and 23')

"""
    Faça um programa que peça o primeiro nome do usuário.
    Se o nome tiver 4 letras ou menos, escreva "Seu nome é muito curto";
    Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"
    Se for maior que 6 letras, escreva "Seu nome é muito grande"
"""

name = input('Type your name: ')
name_length = len(name)

if name_length <= 4:
    print('Your name is too short')
elif name_length <= 6:
    print('Your name is normal')
else:
    print('Your name is too long')