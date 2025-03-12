import random

# Tamanho da grelha
GRID_SIZE = 5

# Inicializar posição da Pyton no centro
pyton_x, pyton_y = GRID_SIZE // 2, GRID_SIZE // 2

# Gerar posição aleatória para a comida, garantindo que não está na posição inicial da Pyton
while True:
    comida_x, comida_y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
    if (comida_x, comida_y) != (pyton_x, pyton_y):
        break  # Sai do loop quando a comida não está na mesma posição da Pyton

def desenhar_tabuleiro():
    """Desenha a grelha do jogo com a Pyton e a comida."""
    for y in range(GRID_SIZE):
        linha = ""
        for x in range(GRID_SIZE):
            if x == pyton_x and y == pyton_y:
                linha += "🐍 "  # Pyton
            elif x == comida_x and y == comida_y:
                linha += "🍎 "  # Comida
            else:
                linha += "⬜ "  # Espaço vazio
        print(linha)
    print("\n")  # Linha em branco para espaçamento

print("🐍 Bem-vindo ao jogo da Pyton! Usa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while True:
    # Mostrar o tabuleiro
    desenhar_tabuleiro()

    # Pedir input do utilizador
    movimento = input("Para onde queres mover a Pyton? (w/a/s/d): ").lower()

    # Atualizar posição com base no input
    if movimento == "w" and pyton_y > 0:
        pyton_y -= 1  # Sobe
    elif movimento == "s" and pyton_y < GRID_SIZE - 1:
        pyton_y += 1  # Desce
    elif movimento == "a" and pyton_x > 0:
        pyton_x -= 1  # Esquerda
    elif movimento == "d" and pyton_x < GRID_SIZE - 1:
        pyton_x += 1  # Direita
    else:
        print("Movimento inválido. Tenta outra direção!")
        continue

    # Verificar se a Pyton apanhou a comida
    if pyton_x == comida_x and pyton_y == comida_y:
        desenhar_tabuleiro()  # Mostrar o último estado
        print("🎉 Parabéns! A Pyton apanhou a comida!")
        break  # Termina o jogo
