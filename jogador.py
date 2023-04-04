#2 ano vespertino
#Alunos: Daniel Guimarães Souza, Danielly Vitória Ferreira da Costa, Luis Henrique Silva Botelho e Marcos Aurélio
#float 
import random

class Jogado:
#class 
    def __init__(self,sexo,nome,time, selecao,passe,fina, ritmo, dribra):
        #atributos
        self.sexo = sexo
        self.nome = nome
        self.time = time
        self.selecao = selecao
        self.passe = passe
        self.fina = fina
        self.ritmo = ritmo
        self.dribra = dribra
    #metodos 
    def imp (self):
        print("="*20)
        print("Nome:"+self.nome)
        print("Seleção:"+self.selecao)
        print("Time:"+self.time)
        print("Sexo:"+self.sexo)
        print("="*20)
        print("Passe:",self.passe)
        print("Finalização:",self.fina)
        print("Ritmo:",self.ritmo)
        print("Drible:", self.dribra)
        print("="*20)

        


    def compara (self, oponente):
        escolha_atribruto = input("Escolha um atributo para comparar\n[1]Drible\n[2]Passe\n[3]Ritmo\nR: ")
        if escolha_atribruto == "1":
            if self.dribra > oponente+self.dribra:
                print("O ganhador é "+self.nome)
                return oponente
            else:
                print("O perdedor é "+self.nome)
                return oponente

        if escolha_atribruto == "2":
            if self.passe > oponente+self.passe:
                print("O ganhador é ",self.nome)
                return oponente
            else:
                print("O perdedor é ",self.nome)
                return oponente
                
        if escolha_atribruto == "3":
            if self.ritmo >  oponente+self.ritmo:
                print("O ganhador é" ,self.nome)
            else:
                print("O perdedor é ",self.nome)
    def sorteia(lista_jogadores):
        numero = random.randint (0,len(lista_jogadores))
        numero -=1
        return numero