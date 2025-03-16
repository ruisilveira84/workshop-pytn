import random

# Tamanho da grelha
GRID_SIZE = 5

# Inicializar posição da Pytn no centro
pytn_x, pytn_y = GRID_SIZE // 2, GRID_SIZE // 2

# Gerar posição aleatória para a comida, garantindo que não está na posição inicial da Pytn
while True:
    comida_x, comida_y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
    if (comida_x, comida_y) != (pytn_x, pytn_y):
        break  # Sai do loop quando a comida não está na mesma posição da Pytn

def desenhar_tabuleiro():
    """Desenha a grelha do jogo com a Pytn e a comida."""
    for y in range(GRID_SIZE):
        linha = ""
        for x in range(GRID_SIZE):
            if x == pytn_x and y == pytn_y:
                linha += "🐍 "  # Pytn
            elif x == comida_x and y == comida_y:
                linha += "🍎 "  # Comida
            else:
                linha += "⬜ "  # Espaço vazio
        print(linha)
    print("\n")  # Linha em branco para espaçamento

print("🐍 Bem-vindo ao jogo da Pytn! \nUsa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while True:
    # Mostrar o tabuleiro
    desenhar_tabuleiro()

    # Pedir input do utilizador
    movimento = input("Para onde queres mover a Pytn? (w/a/s/d): ").lower()

    # Atualizar posição com base no input
    if movimento == "w" and pytn_y > 0:
        pytn_y -= 1  # Sobe
    elif movimento == "s" and pytn_y < GRID_SIZE - 1:
        pytn_y += 1  # Desce
    elif movimento == "a" and pytn_x > 0:
        pytn_x -= 1  # Esquerda
    elif movimento == "d" and pytn_x < GRID_SIZE - 1:
        pytn_x += 1  # Direita
    else:
        print("Movimento inválido. Tenta outra direção!")
        continue

    # Verificar se a Pytn apanhou a comida
    if pytn_x == comida_x and pytn_y == comida_y:
        desenhar_tabuleiro()  # Mostrar o último estado
        print("🎉 Parabéns! A Pytn apanhou a comida!")
        break  # Termina o jogo
