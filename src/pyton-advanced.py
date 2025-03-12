import random
import time  # Para medir o tempo do jogador

# Tamanho da grelha
GRID_SIZE = 5

# Inicializar posição da Pyton no centro
pyton_x, pyton_y = GRID_SIZE // 2, GRID_SIZE // 2

# Função para gerar uma nova fruta (garantindo que não está na mesma posição da Pyton)
def gerar_fruta():
    while True:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if (x, y) != (pyton_x, pyton_y):
            return x, y

# Inicializa a primeira fruta
comida_x, comida_y = gerar_fruta()

# Contador de frutas apanhadas
frutas_apanhadas = 0
total_frutas = 3  # O jogador precisa de apanhar 3 frutas para ganhar

# Começa a contar o tempo
tempo_inicio = time.time()

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
    print(f"\n🍎 Frutas apanhadas: {frutas_apanhadas}/{total_frutas}\n")

print("🐍 Bem-vindo ao Pyton Advanced! Tens de apanhar 3 frutas para ganhar! 🍎🍎🍎")
print("Usa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while frutas_apanhadas < total_frutas:
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
        frutas_apanhadas += 1
        print(f"🎉 A Pyton apanhou uma fruta! ({frutas_apanhadas}/{total_frutas})")
        
        # Se ainda não apanhou todas as frutas, gera uma nova
        if frutas_apanhadas < total_frutas:
            comida_x, comida_y = gerar_fruta()

# O jogo terminou, calcular tempo total
tempo_fim = time.time()
tempo_total = round(tempo_fim - tempo_inicio, 2)

# Mensagem final
desenhar_tabuleiro()
print(f"🏆 Parabéns! A Pyton apanhou todas as frutas em {tempo_total} segundos! 🎉")
