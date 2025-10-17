from random import choice
from time import sleep

jogada = str(input('Escolha [C] cara e [K] coroa: ')).strip().upper()
while True:
    if jogada not in ['C', 'K']:
        print('Jogada inválida!')
        jogada = str(input('Escolha [C] cara e [K] coroa: ')).strip().upper()
        continue
    print('Jogo iniciado...')
    sleep(1)
    print('Jogada do computador...')
    sleep(1)
    computador = choice(['C', 'K'])
    print(f'O computador jogou {computador}.')
    if jogada == computador:
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    break