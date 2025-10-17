from random import randint
from time import sleep
print('==' * 20)
print('\033[1m------------Adivinhe o número-----------\033[m')
print('==' * 20)
r = 0
conttent = 1
computador = randint(0, 1000)
print('Eu pensei em um número entre 0 e 30 \nvocê consegue acertar que número é.')
sleep(1)
while r != computador:
    r = int(input('Digite um valor: '))
    if r != computador:
        conttent = conttent+1
        if r < computador:
            sleep(1)
            print('\033[31mMais...\033[m')
        if r > computador:
            sleep(1)
            print('\033[31mMenos...\033[m')
        if r == computador:
            print('Parabéns! você venceu')
sleep(1)
print('\033[32mParabéns! você venceu\033[m')
print('você precisou de {} tentativas'.format(conttent))
print()
input('Pressione <enter> para continuar')
