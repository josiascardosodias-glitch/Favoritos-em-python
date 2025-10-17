print('\033[;33m-=-\033[m' * 20)
print('\033[2;36mAnalisador de Tiangulos\033[m.2.0')
print('\033[;33m-=-\033[m' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('CARREGANDO.....')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[2;32mOs segmentos acima podem formar um triângulo\033[m.', end=' ')
    if r1 == r2 == r3:
        print('\033[;34mequilátero\033[m.')
    elif r1 != r2 != r3 != r1:
        print('\033[2;34mescaleno\033[m.')
    else:
        print('\033[2;34misóceles\033[m.')
else:
    print('\033[2;31mOs segmentos acima não podem formar um triângulo\033[m.')
print()
input('Pressione <enter> para continuar')
