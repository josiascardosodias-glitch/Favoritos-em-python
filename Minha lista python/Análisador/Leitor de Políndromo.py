frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('A frase {} de trás para frente fica {}'.format(frase, inverso))
if inverso == junto:
    print('Sua frase é um palíndromo!')
else:
    print('A frase sua não possue um palíndromo!')
print()
input('Pressione <enter> para continuar')
