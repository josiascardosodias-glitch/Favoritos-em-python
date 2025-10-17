print('==' * 20)
print('\033[1m               TABUADA 2.0\033[m')
print('==' * 20)
n = int(input('Digite um número para saber a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n * c)))
print()
input('Pressione <enter> para continuar')
