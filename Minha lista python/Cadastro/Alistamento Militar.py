from datetime import date
ano = int(input('Informe o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print('==' * 30)
    print('\033[2;32mMeus parabéns!!, você já tem {} e está na idade pra servir \033[m'.format(idade))
    print('==' * 30)
elif idade < 18:
    saldo1  = (idade - 18) * -1
    print('Você ainda tem {}, então só tera que se alistar daqui {} anos.'.format(idade, saldo1))
    ano = atual + saldo1
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo2 = idade - 18
    print('Você já tem {}, deveria ter que ter se alistado a {} anos.'.format(idade, saldo2))
    ano = atual - saldo2
    print('Seu ano de alistamento foi em {}'.format(ano))
print()
input('Pressione <enter> para continuar')
