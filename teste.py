import random
class Jogado:
    def __init__(self,sexo,nome,time, selecao,passe,fina, ritmo, dribra):
        self.sexo = sexo
        self.nome = nome
        self.time = time
        self.selecao = selecao
        self.passe = passe
        self.fina = fina
        self.ritmo = ritmo
        self.dribra = dribra

    def imp (self):
        print("="*20)
        print("Nome: "+self.nome)
        print("Seleção: "+self.selecao)
        print("Time: "+self.time)
        print("Sexo: "+self.sexo)
        print("="*20)
        print("Passe: ",self.passe)
        print("Finalização: ",self.fina)
        print("Ritmo: ",self.ritmo)
        print("Drible: ", self.dribra)
        print("="*20)

        


    def compara (self, oponente):
        escolha_atributo = input("Escolha um atributo para comparar")
        if escolha_atributo == "1":
            if self.dribra > oponente.dribra:
                print("O ganhador é "+self.nome)
            else:
                print("O ganhador é "+oponente.nome)
        elif escolha_atributo == "2":
            if self.passe > oponente.passe:
                print("O ganhador é "+self.nome)
            else:
                print("O ganhador é "+oponente.nome)
        elif escolha_atributo == "3":
            if self.ritmo < oponente.ritmo:
                print("O ganhador é" +self.nome)
            else:
                print("O ganhador é "+oponente.nome)





