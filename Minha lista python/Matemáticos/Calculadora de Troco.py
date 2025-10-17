print('==' * 20)
print('           Banco Do JOSIAS')
print('==' * 20)
valor = int(input('Qual o valor do produto? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('==' * 20)
print()
input('<Pressione qualquer tecla para sair>')
