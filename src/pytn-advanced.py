import random
import time
import os

# Tamanho da grelha
GRID_SIZE = 5
LEADERBOARD_FILE = "leaderboard.txt"  # Nome do ficheiro onde guardamos os tempos

# Pedir nome do jogador
nome_jogador = input("👤 Escreve o teu nome: ")

# Inicializar posição da Pytn no centro
pytn_x, pytn_y = GRID_SIZE // 2, GRID_SIZE // 2

# Função para gerar uma nova fruta (garantindo que não está na mesma posição da Pytn)
def gerar_fruta():
    while True:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if (x, y) != (pytn_x, pytn_y):
            return x, y

# Inicializa a primeira fruta
comida_x, comida_y = gerar_fruta()

# Contador de frutas apanhadas
frutas_apanhadas = 0
total_frutas = 3  # O jogador precisa de apanhar 3 frutas para ganhar

# Começa a contar o tempo
tempo_inicio = time.time()

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
    print(f"\n🍎 Frutas apanhadas: {frutas_apanhadas}/{total_frutas}\n")

print(f"🐍 Bem-vindo, {nome_jogador}! O teu objetivo é apanhar 3 frutas! 🍎🍎🍎")
print("Usa 'w' (cima), 's' (baixo), 'a' (esquerda) e 'd' (direita) para mover.")

while frutas_apanhadas < total_frutas:
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
        frutas_apanhadas += 1
        print(f"🎉 A Pytn apanhou uma fruta! ({frutas_apanhadas}/{total_frutas})")
        
        # Se ainda não apanhou todas as frutas, gera uma nova
        if frutas_apanhadas < total_frutas:
            comida_x, comida_y = gerar_fruta()

# O jogo terminou, calcular tempo total
tempo_fim = time.time()
tempo_total = round(tempo_fim - tempo_inicio, 2)

# Mensagem final
desenhar_tabuleiro()
print(f"🏆 Parabéns, {nome_jogador}! A Pytn apanhou todas as frutas em {tempo_total} segundos! 🎉")

# Função para guardar e mostrar a leaderboard com nome e tempo
def atualizar_leaderboard(nome, tempo):
    # Ler tempos anteriores
    tempos = []
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            for linha in file.readlines():
                try:
                    nome_antigo, tempo_antigo = linha.strip().split(" - ")
                    tempos.append((nome_antigo, float(tempo_antigo)))
                except ValueError:
                    continue  # Ignorar linhas mal formatadas

    # Adicionar o novo tempo e ordenar
    tempos.append((nome, tempo))
    tempos.sort(key=lambda x: x[1])  # Ordenar pelo tempo (menor é melhor)

    # Guardar apenas os top 5 tempos
    with open(LEADERBOARD_FILE, "w") as file:
        for jogador, t in tempos[:5]:
            file.write(f"{jogador} - {t}\n")

    # Mostrar a leaderboard
    print("\n🏅 **Leaderboard - Top 5 Tempos** 🏅")
    for i, (jogador, t) in enumerate(tempos[:5], start=1):
        print(f"{i}º lugar: {jogador} - {t} segundos")

# Atualizar e mostrar a leaderboard
atualizar_leaderboard(nome_jogador, tempo_total)
