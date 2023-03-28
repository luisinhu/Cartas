from tkinter import *

class Jogador:
    def __init__(self, nome, sexo, time, selecao):
        self.nome = nome
        self.sexo = sexo
        self.time = time
        self.selecao = selecao

    def card(self):
        carta = Tk()
        texto = "JOGADORES"
        carta.title(self.nome)
        carta.geometry("350x450")
        carta.resizable(False, False)

        caixa_texto=Label(carta, text= texto)
        caixa_texto.pack()
        imgJogador = PhotoImage(file="images/"+self.nome+".png")
        label = Label(carta, image=imgJogador)
        label.pack()
        carta.mainloop()
