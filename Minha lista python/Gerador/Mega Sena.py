from random import randint
from time import sleep
lista = list()
jogos = list()
print('=Lista de chutes da MEGA SENA=')
print('=-' * 25)
quant = int(input('Quantos jogos deseja fazer? '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('=-' * 20)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte!')
print()

input('<Pressione qualquer tecla para sair>')
