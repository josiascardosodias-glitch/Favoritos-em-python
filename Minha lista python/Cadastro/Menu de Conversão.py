num = int(input('Digite um número inteiro:'))
print('==' * 20)
print('''escolha uma das bases de conversão
[1] Binario
[2] Octal
[3] Hexadecimal''')
opção = int(input('Digite uma das opções:'))
print('==' * 20)
print('CARREGANDO...')
if opção == 1:
    print('O número {} em Binario será {}.'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} na forma Octal será {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} na forma Hexadecimal será {}.'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')
print()
input('Pressione <enter> para continuar')
