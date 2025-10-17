from time import sleep
print('==' * 10)
print("\033[1m-Leitor de números-\033[m")
print('==' * 10)
r = 0
while r != 5:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('''O que deseja fazer 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    r = int(input('Digite a opção escolhida: '))
    if r == 1:
        s = n1 + n2
        sleep(1)
        print('A soma entre {} e {} é = {}'.format(n1, n2, s))
    if r == 2:
        s = n1 * n2
        sleep(1)
        print('A multiplicação entre {} e {} é = {}'.format(n1, n2, s))
    if r == 3:
        if n1 > n2:
            sleep(1)
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        if n1 == n2:
            sleep(1)
            print('Entre {} e {} não á número maior'.format(n1, n2))
        if n1 < n2:
            sleep(1)
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))
    if r == 4:
        pass
print('==' * 20)
print("\033[1mPrograma finalizado com sucesso!\033[m")
print('==' * 20)
print()
input('Pressione <enter> para continuar')
