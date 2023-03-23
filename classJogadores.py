from tkinter import *

class Jogador:
    def __init__(self,sexo,nome,time, selecao):
        self.sexo = sexo
        self.nome = nome
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
