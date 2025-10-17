print('-_-_\033[m' * 10)
print('\033[2;34mMEDIDOR DE IMC\033[m')
print('-_-_\033[m' * 10)
altura = float(input('Insira a sua altura: '))
peso = float(input('Insira a sua peso: '))
print('CARREGANDO...')
print('==' * 20)
imc = peso / ( altura * altura )
print('O seu IMC é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está \033[2;34mabaixo do peso\033[m.')
elif 18.5 <= imc <= 25:
    print('Você está no \033[2;32mpeso ideal\033[m.')
elif 25 <= imc <= 30:
    print('Você está \033[2;33msobrepeso\033[m.')
elif 30 <= imc <= 40:
    print('Você está em \033[2;31mobesidade\033[m.')
elif imc > 40:
    print('Você está em \033[2;37mobesidade mórbida\033[m.')
print()
input('Pressione <enter> para continuar')
