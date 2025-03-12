# ----------------------------------------------------------

# Workshop de Python com a Pytn:

# Neste workshop, vais criar um jogo simples onde controlas a Pytn (🐍), uma cobra que precisa de apanhar uma maçã (🍎) num tabuleiro.
# Vais precisar de desenhar o tabuleiro, permitir que o jogador mova a cobra e verificar se a comida foi apanhada.
# Segue as dicas para completar o código do teu jogo!

# ----------------------------------------------------------

import random

# Tamanho da grelha
GRID_SIZE = 5

# Inicializar posição da Pytn no centro
pytn_x, pytn_y = GRID_SIZE // 2, GRID_SIZE // 2

# Gerar posição aleatória para a comida, garantindo que não está na posição inicial da Pytn
# Dica: Usa um loop para garantir que a comida não nasce na mesma posição da Pytn.
comida_x, comida_y = None, None

# TODO: Implementar a função desenhar_tabuleiro()
def desenhar_tabuleiro():
    """Desenha a grelha do jogo com a Pytn e a comida."""
    pass  # Dica: Usa loops aninhados para desenhar a grelha (🐍,🍎,⬜)

print("🐍 Bem-vindo ao jogo da Pytn! Usa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while True:
    # TODO: Chamar a função para mostrar o tabuleiro
    # desenhar_tabuleiro()
    
    # Pedir input do utilizador
    movimento = input("Para onde queres mover a Pytn? (w/a/s/d): ").lower()
    
    # TODO: Atualizar a posição da Pytn com base no input do utilizador
    # Dica: Usa condições if para verificar qual direção foi escolhida.
    
    # TODO: Verificar se a Pytn apanhou a comida
    # Dica: Se as coordenadas de Pytn e da comida forem iguais, o jogador ganhou.
    
    # TODO: Mostrar mensagem de vitória e sair do loop se a comida for apanhada.
    pass
