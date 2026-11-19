import tkinter as tk
import random

# Configurações
LARGURA = 600
ALTURA = 400
TAMANHO = 20
VELOCIDADE = 130

# Janela
janela = tk.Tk()
janela.title("Jogo da Cobrinha")
janela.resizable(False, False)

canvas = tk.Canvas(
    janela,
    width=LARGURA,
    height=ALTURA,
    bg="black"
)
canvas.pack()

# Cobra
cobra = [
    [300, 200],
    [280, 200],
    [260, 200]
]

# Direção
direcao = "Direita"

# Comida
comida = [
    random.randrange(0, LARGURA, TAMANHO),
    random.randrange(0, ALTURA, TAMANHO)
]

# Estado do jogo
game_over = False


# Mudar direção
def mudar_direcao(nova_direcao):
    global direcao

    # Impede a cobra de voltar sobre si mesma
    if nova_direcao == "Cima" and direcao != "Baixo":
        direcao = "Cima"

    elif nova_direcao == "Baixo" and direcao != "Cima":
        direcao = "Baixo"

    elif nova_direcao == "Esquerda" and direcao != "Direita":
        direcao = "Esquerda"

    elif nova_direcao == "Direita" and direcao != "Esquerda":
        direcao = "Direita"


# Movimentar a cobra
def mover():
    global comida, game_over

    if game_over:
        return

    # Cria uma cópia da cabeça
    cabeca = cobra[0].copy()

    # Movimenta a cabeça
    if direcao == "Cima":
        cabeca[1] -= TAMANHO

    elif direcao == "Baixo":
        cabeca[1] += TAMANHO

    elif direcao == "Esquerda":
        cabeca[0] -= TAMANHO

    elif direcao == "Direita":
        cabeca[0] += TAMANHO

    # Colisão com a parede
    if (
        cabeca[0] < 0
        or cabeca[0] >= LARGURA
        or cabeca[1] < 0
        or cabeca[1] >= ALTURA
    ):
        fim_de_jogo()
        return

    # Colisão com o próprio corpo
    if cabeca in cobra:
        fim_de_jogo()
        return

    # Adiciona a nova cabeça
    cobra.insert(0, cabeca)

    # Comeu a comida
    if cabeca == comida:
        comida = [
            random.randrange(0, LARGURA, TAMANHO),
            random.randrange(0, ALTURA, TAMANHO)
        ]

    else:
        # Remove a cauda
        cobra.pop()

    # Desenha novamente
    desenhar()

    # Continua o jogo
    janela.after(VELOCIDADE, mover)


# Desenhar o jogo
def desenhar():
    canvas.delete("all")

    # Desenha a comida
    canvas.create_oval(
        comida[0],
        comida[1],
        comida[0] + TAMANHO,
        comida[1] + TAMANHO,
        fill="red"
    )

    # Desenha a cobra
    for i, bloco in enumerate(cobra):

        if i == 0:
            cor = "blue"
        else:
            cor = "purple"

        canvas.create_rectangle(
            bloco[0],
            bloco[1],
            bloco[0] + TAMANHO,
            bloco[1] + TAMANHO,
            fill=cor,
            outline="black"
        )


# Fim de jogo
def fim_de_jogo():
    global game_over

    game_over = True

    canvas.create_text(
        LARGURA // 2,
        ALTURA // 2,
        text="FIM DE JOGO",
        fill="red",
        font=("Arial", 30, "bold")
    )

    canvas.create_text(
        LARGURA // 2,
        ALTURA // 2 + 40,
        text="Pressione ENTER para jogar novamente",
        fill="white",
        font=("Arial", 14)
    )


# Reiniciar o jogo
def reiniciar(event=None):
    global cobra, comida, direcao, game_over

    if not game_over:
        return

    cobra = [
        [300, 200],
        [280, 200],
        [260, 200]
    ]

    direcao = "Direita"

    comida = [
        random.randrange(0, LARGURA, TAMANHO),
        random.randrange(0, ALTURA, TAMANHO)
    ]

    game_over = False

    desenhar()
    mover()


# Teclas
janela.bind(
    "<a>",
    lambda event: mudar_direcao("Esquerda")
)

janela.bind(
    "<d>",
    lambda event: mudar_direcao("Direita")
)

janela.bind(
    "<w>",
    lambda event: mudar_direcao("Cima")
)

janela.bind(
    "<s>",
    lambda event: mudar_direcao("Baixo")
)

janela.bind(
    "<Return>",
    reiniciar
)

# Começa o jogo
desenhar()
mover()

janela.mainloop()