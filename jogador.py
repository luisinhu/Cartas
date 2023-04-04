#informática
#2 ano vespertino
#Programação Orientada a Objetos
#Alunos: Daniel Guimarães Souza, Danielly Vitória Ferreira da Costa, Luis Henrique Silva Botelho e Marcos Aurélio

import random

class Jogado:
#class 
    def __init__(self,sexo,nome,time, selecao,passe,fina, ritmo, dribra, defesa, fisico):
        #atributos
        self.sexo = sexo
        self.nome = nome
        self.time = time
        self.selecao = selecao
        self.passe = passe
        self.fina = fina
        self.ritmo = ritmo
        self.dribra = dribra
        self.defesa=defesa
        self.fisico=fisico
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
        print("Defesa:", self.defesa)
        print("Fisico:", self.fisico)
        print("="*20)

        


    def compara (self, oponente):
        escolha_atribruto = input("Escolha um atributo para comparar\n[1]Drible\n[2]Passe\n[3]Ritmo\n[4]Finalização\n[5]Físico\n[6]Defesa\nR: ")
        if escolha_atribruto == "1":
            if oponente+self.dribra > self.dribra:
                print(f"{self.nome} é o ganhador")
                return oponente
            elif self.dribra > oponente+self.dribra:
                print(f"{self.nome} é o ganhador")
                return oponente
            else:
                print(f"{self.nome} é o perdedor ")
                return oponente

        if escolha_atribruto == "2":
            if oponente+self.passe > self.passe:
                print(f"{self.nome} o é ganhador  ")
                return oponente
            elif self.passe > oponente+self.passe:
                print(f"{self.nome} é o ganhador")
                return oponente
            
            else:
                print(f"{self.nome} é o  perdedor  ")
                return oponente
                
        if escolha_atribruto == "3":
            if oponente+self.ritmo > self.ritmo:
                print(f"{self.nome} é o ganhador ")
                return oponente
            elif self.ritmo > oponente+self.ritmo:
                print(f"{self.nome} é o ganhador")
                return oponente
            
            else:
                print("O perdedor é ",self.nome)
                return oponente
        if escolha_atribruto == "4":
            if oponente+self.fina > self.fina:
                print(f"{self.nome} é o ganhador")
                return oponente
            elif self.fina > oponente+self.fina:
                print(f"{self.nome} é o ganhador")
                return oponente
            
            else:
                print(f"{self.nome} é o perdedor")
                return oponente
        
        if escolha_atribruto == "5":
            if  oponente+self.fisico > self.fisico:
                print(f"{self.nome} é o ganhador")
                return oponente
            elif self.fisico > oponente+self.fisico:
                print(f"{self.nome} é o ganhador")
                return oponente
            
            else:
                print(f"{self.nome} é o perdedor")
                return oponente
        
        if escolha_atribruto == "6":
            if oponente+self.defesa > self.defesa:
                print(f"{self.nome} é o ganhador")
                return oponente
            elif self.defesa > oponente+self.defesa:
                print(f"{self.nome} é o ganhador")
                return oponente
            else:
                print(f"{self.nome} é o perdedor")
                return oponente
