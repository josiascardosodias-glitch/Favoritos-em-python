#Cronometro V.1.0

from time import sleep

def leiaInt(msg):
    valor = False
    while not valor:
        entrada = str(input(msg)).strip()
        if entrada.isnumeric():
            return int(entrada)
        else:
            print('\033[;31mERRO! O valor digitado não é um número válidio\033[m')


while True:
    print('''TABELA DE OPÇÕES:\n[1] Começar Contagem\n[2] sair''')
    op = leiaInt('Escolha uma opção: ')
    if op == 1:
        n = leiaInt('Digite um número: ')
        for c in range(n, -1, -1):
            print(c)
            sleep(1)
        print('FIM!')
        sleep(1)
    elif op == 2:
        print('Saindo...')
        break
    else:
        print('\033[;31mERRO! Digite uma opção válida\033[m')
