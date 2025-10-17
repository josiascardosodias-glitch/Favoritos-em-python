from time import sleep
from random import randint

print('\033[1m-=' * 15)
print('JOGO DO PAR OU ÍMPAR')
print('-=' * 15)
soma = jogador = 0
cont = 0

while True:
    if soma % 2 == 0 and jogador == 'I' or soma % 2 == 1 and jogador == 'P':
         break
    num = int(input('Digite um número: '))
    print('Você quer par ou impar')
    jogador = " "
    while jogador not in 'PI':
        jogador = str(input('Selecione uma das opções [P/I]: ')).strip().upper()[0]
    print('==' * 15)
    computador = randint(0, 10)
    soma = computador + num
    sleep(1)
    print('PAR.')
    sleep(1)
    print('OU..')
    sleep(1)
    print('IMPAR...')
    sleep(0.5)
    print(f'Você jogou {num} e o computador jogou {computador} = {soma}.')
    sleep(0.5)
    if soma % 2 == 0 and jogador == 'P':
        print('\033[32mvocê venceu\033[m!')
        cont += 1
    if soma % 2 == 1 and jogador == 'P':
        print('\033[31mGame over!.\033[m')
    if soma % 2 == 1 and jogador == 'I':
        print('\033[32mvocê venceu\033[m!')
        cont += 1
    if soma % 2 == 0 and jogador == 'I':
        print('\033[31mGame over\033[m!.')
    print('--' * 15)

sleep(0.5)
print(f'você fez \033[34m{cont}\033[m pontos.')
print('==' * 15)
print()
input('Pressione <enter> para continuar')
