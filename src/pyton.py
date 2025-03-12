import random

# Tamanho da grelha
GRID_SIZE = 5

# Inicializar posição da cobra no centro
cobra_x, cobra_y = GRID_SIZE // 2, GRID_SIZE // 2

# Gerar posição aleatória para a comida, garantindo que não está na posição inicial da cobra
while True:
    comida_x, comida_y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
    if (comida_x, comida_y) != (cobra_x, cobra_y):
        break  # Sai do loop quando a comida não está na mesma posição da cobra

def desenhar_tabuleiro():
    """Desenha a grelha do jogo com a cobra e a comida."""
    for y in range(GRID_SIZE):
        linha = ""
        for x in range(GRID_SIZE):
            if x == cobra_x and y == cobra_y:
                linha += "🐍 "  # Cobra
            elif x == comida_x and y == comida_y:
                linha += "🍎 "  # Comida
            else:
                linha += "⬜ "  # Espaço vazio
        print(linha)
    print("\n")  # Linha em branco para espaçamento

print("Bem-vindo ao Jogo da Cobrinha! Usa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while True:
    # Mostrar o tabuleiro
    desenhar_tabuleiro()

    # Pedir input do utilizador
    movimento = input("Para onde queres ir? (w/a/s/d): ").lower()

    # Atualizar posição com base no input
    if movimento == "w" and cobra_y > 0:
        cobra_y -= 1  # Sobe
    elif movimento == "s" and cobra_y < GRID_SIZE - 1:
        cobra_y += 1  # Desce
    elif movimento == "a" and cobra_x > 0:
        cobra_x -= 1  # Esquerda
    elif movimento == "d" and cobra_x < GRID_SIZE - 1:
        cobra_x += 1  # Direita
    else:
        print("Movimento inválido. Tenta outra direção!")
        continue

    # Verificar se a cobra apanhou a comida
    if cobra_x == comida_x and cobra_y == comida_y:
        desenhar_tabuleiro()  # Mostrar o último estado
        print("🎉 Parabéns! Apanhaste a comida!")
        break  # Termina o jogo
    