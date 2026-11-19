import tkinter as tk
import random

configuração da janela principal
janela = tk.TK()
janela.title("jogo simples comn tinker")
janela.rezable(False,False)

#configuração de canvas (áreas de desenho)
LARGURA = 600
ALTURA = 400
canvas = tk.Canvas(janela,width=LARGURA,heigth=ALTURA,bg="black")
canvas.pack()

#váriaveis do jogo
pontos=0

#criação dos personagens(jogador e comida)
jogador = canvas.create_rectangle(50,150,80,180,fill="cyan")
comida = canvas.create_rectangle(0,0,20,20,fill="red")

def mover_comida():
    """move a comida para uma posição aleatória na tela."""
    x = random.randint(20,LARGURA - 20)
    y = random.randint(20,ALTURA - 20)
    canvas.coords(comida,x,y,x+y+20,y+20)
    
    #posiciona a primeira comida
    mover_comida()
    
    #texto do placar
    placr = canvas.create_text(50,20,text=f"Pontos:{pontos}",fill="white",font=("arial",14))
    
    def verificar_colisao():
        """verifica se o jogador encostou na comida."""
        global pontos
        pos_jogador = canvas.coords(jogador)
        pos_comida = canvas.coords(comida)
        
        #checa sobreposição de retângulos
        if (pos_jogador[2] >=pos_comida[0]and 
        pos_jogador[0]<=pos_comida[2]and)
        
         if (pos_jogador[3] >=pos_comida[0]and 
        pos_jogador[1]<=pos_comida[3]):
             
             pontos +=1
             
             canvas.itemconfig(placar,text=f"pontos:{pontos}")
             mover_comida()
             
             def mover(event):
                """controla o movimento do jogador pelas setas do teclado."""
                tecla = event.keysym
                passo = 20
                pos = canvas.coords(jogador)
                
                if tela == "up" and pos[1] > 0:
                    canvas.move(jogador,0,-passo)
                    
                elif == "down" and pos[3] < ALTURA:
                    
                    canvas.move(jogador,0,passo)
                elif  tecla == "left" and pos[0] > 0:
                    canvas.move(jogador,-passo,0)
                    
                elif tecla == "rigth" and pos[2] < LARGURA:
                    
                    canvas.move(jogador,passo,0)
                    
                    verificar_colisao()
                    
                    #vincula as teclas de setas ao jogo
                    janela.bind("<keypress>",mover)
                    
                    #inicia o loop da interface gráfica
                    janela.mainloop()