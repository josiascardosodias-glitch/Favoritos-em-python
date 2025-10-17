lista = ['Montanha', 'Espelho', 'Biblioteca', 'Sofá', 'Rio', 'Lâmpada', 'Floresta', 'Chave', 'Museu', 'Mesa', 'Jardim', 'Caderno',
'Farol', 'Porta', 'Praia', 'Escada', 'Livro', 'Janela', 'Castelo', 'Relógio', 'Ponte', 'Caneta', 'Sala', 'Tapete', 'Deserto', 'Mapa', 'Vela',
'Igreja', 'Cadeira', 'Cidade', 'Óculos', 'Floresta', 'Barco', 'Garfo', 'Ponte', 'Teatro', 'Prato', 'Montanha-russa', 'Avião', 'Cama',
'Rua', 'Geladeira', 'Farol', 'Mesa', 'Caneta', 'Chave', 'Jardim', 'Espelho', 'Museu', 'Janela', ]

def gerar_palavra():
    import random
    palavra_aleatoria = random.choice(lista)
    return palavra_aleatoria

def reiniciar_gerador():
    while True:
        resposta = input("Deseja gerar outra palavra? (s/n): ").strip().lower()
        if resposta == 's':
            print(gerar_palavra())
        elif resposta == 'n':
            print("Encerrando o gerador de palavras.")
            break
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")

print(gerar_palavra())
reiniciar_gerador()
