from datetime import datetime
trabalhador = {}

trabalhador['nome'] = str(input('Digite seu nome: '))
nasc = int(input('Digite o ano do seu nascimento: '))
idade = datetime.now().year - nasc
trabalhador['idade'] = idade
trabalhador['ctps'] = int(input('Digite sua ctps(0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contrato'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = int(input('Salário: '))
    trabalhador['aposentadoria'] = idade + (35 - (datetime.today().year - trabalhador['contrato']))

print('=-'*20)
for k, v in trabalhador.items():
    print(f'    => {k} tem o valor {v}')

input('Pressione <enter> para sair')
