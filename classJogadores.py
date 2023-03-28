from tkinter import *

class Jogador:
    def __init__(self, nome, sexo, time, selecao):
        self.nome = nome
        self.sexo = sexo
        self.time = time
        self.selecao = selecao

    def card(self):
        carta = Tk()
        carta.title(self.nome)
        carta.geometry("247x350")
        carta.resizable(False, False)


        imgJogador = PhotoImage(file="images/"+self.nome+".png")
        label = Label(carta, image=imgJogador)
        label.pack()
        carta.mainloop()
