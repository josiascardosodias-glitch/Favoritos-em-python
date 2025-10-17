from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
resultados = {}
placar = []
print('Valores sorteados:')
for c in range(1, 5):
    resultados[f'{c}'] = randint(1, 6)
    sleep(1.5)
    print(f'O jogador N° {c} jogou: {resultados[f'{c}']} no dado')
print('-'*30)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: jogador {v[0]} com {v[1]} pontos')
    sleep(1.5)

input('Pressione <enter> para sair')
