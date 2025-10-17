ficha = []
lista = []
while True:
    nome = str(input('Nome: '))
    nota1 =(float(input('Nota 1: ')))
    nota2 =(float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Resposta [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Mêdia":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 para parar) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte sempre >>>')
print()
print('<Pressione qualquer tecla para sair>')
