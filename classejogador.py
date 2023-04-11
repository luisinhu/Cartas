#informática
#2 ano vespertino
#Programação Orientada a Objetos
#Alunos: Daniel Guimarães Souza 
#Danielly Vitória Ferreira da Costa 
#Luis Henrique Silva Botelho 
#Marcos Aurélio
class Jogado:
#class 
  #construtor
    def __init__(self,nome,sexo,time,passe,fina, ritmo, drible, defesa, fisico):
        #atributos
        self.nome = nome
        self.sexo = sexo
        self.time = time
        self.passe = passe
        self.fina = fina
        self.ritmo = ritmo
        self.drible = drible
        self.defesa=defesa
        self.fisico=fisico
    #função de mostrar a carta 
    def imprimir (self):
        print("="*15)
        print(f"Nome:{self.nome}")
        print(f"Sexo:{self.sexo}")
        print(f"Time:{self.time}")
        print(f"Passe:{self.passe}")
        print(f"Finalização:{self.fina}")
        print(f"Rtimo:{self.ritmo}")
        print(f"Drible:{self.drible}")
        print(F"Defesa:{self.defesa}")
        print(f"Físico:{self.fisico}")
        print("="*15)        
    #função de comparar qual atributo é maior
    def compara (self, oponente):
        escolha_atribruto = input("Escolha um atributo para comparar\n[1]Drible\n[2]Passe\n[3]Ritmo\n[4]Finalização\n[5]Físico\n[6]Defesa\nR: ")
        while escolha_atribruto != 1 and escolha_atribruto !=2 and escolha_atribruto != 3 and escolha_atribruto != 4 and escolha_atribruto != 5 and escolha_atribruto != 6:
          print("Erro! número não reconhecido!")
          escolha_atribruto = input("Escolha um atributo para comparar\n[1]Drible\n[2]Passe\n[3]Ritmo\n[4]Finalização\n[5]Físico\n[6]Defesa\nR: ") 
        if escolha_atribruto == "1":
          if self.drible > oponente.drible:
              print(f"{self.nome} tem o drible {self.drible} maior que o drible de {oponente.nome} que é {oponente.drible}")
              return oponente
          elif self.drible == oponente.drible:
            print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.drible}")
            return oponente

          else:
            print(f"{oponente.nome} tem o drible {oponente.drible} maior que o drible de {self.nome} que tem o valor de {self.drible}")
            return oponente

        if escolha_atribruto == "2":
          if self.passe > oponente.passe:
              print(f"{self.nome} tem o passe {self.passe} maior que o passe de {oponente.nome} que é {oponente.passe} ")
              return oponente
          elif self.passe == oponente.passe:
            print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.passe}")
            return oponente
            
          else:
            print(f"{oponente.nome} tem o passe {oponente.passe} maior que o passe de {self.nome} que é {self.passe}  ")
            return oponente
                
        if escolha_atribruto == "3":
          if self.ritmo > oponente.ritmo:
            print(f"{self.nome} tem o ritmo {self.ritmo} maior que o ritmo de{oponente.nome} que é {oponente.ritmo} ")
            return oponente
          elif self.passe == oponente.passe:
            print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.passe}")
            return oponente
            
            
          else:
              print(f"{oponente.nome} tem o ritmo {oponente.ritmo} mairo que o ritmo de {self.nome} que é {self.ritmo}")
              return oponente
        if escolha_atribruto == "4":
          if self.fina > oponente.fina:
            print(f"{self.nome} tem a finalização {self.fina} maior que a finalização de {oponente.nome} que é {oponente.fina} ")
            return oponente
          elif self.fina == oponente.fina:
            print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.fina}")
            return oponente
          else:
            print(f"{oponente.nome} tem a finalização {oponente.fina} maior que a finalização de {self.nome} que é {self.fina}")
            return oponente
        
        if escolha_atribruto == "5":
            if  self.fisico > oponente.fisico:
              print(f"{self.nome} tem o físico {self.fisico} maior que o físico de {oponente.nome} que é {oponente.fisico}")
              return oponente
            elif self.fisico == oponente.fisico:
              print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.fisico}")
              return oponente
    
            
            else:
                print(f"{oponente.nome} tem o físico {oponente.fisico} maior que o físico de {self.nome} que é {self.fisico}")
                return oponente
        
        if escolha_atribruto == "6":
            if self.defesa > oponente.defesa:
              print(f"{self.nome} tem a defesa {self.defesa} maior que a defesa de {oponente.nome} que é {oponente.defesa}")
              return oponente
            elif self.defesa == oponente.defesa:
              print(f"{self.nome} empatou com o(a) oponente {oponente.nome} no atributo {self.defesa} ")
           
            else:
              print(f"{oponente.nome} tem a defesa {oponente.defesa} maior que a defesa de {self.nome} que é {self.defesa}")
              return oponente
     #função de fazer a competição e mostrar o ganhador -Dani
    def definindo_ganhador(self, oponente):
      escolher = int(input("Escolha um atributo para competir\n[1]Drible\n[2]Passe\n[3]Ritmo\n[4]Finalização\n[5]Físico\n[6]Defesa\nR: "))
      while escolher != 1 and escolher !=2 and escolher != 3 and escolher != 4 and escolher != 5 and escolher != 6:
        print("Erro! tente colocar um número correto")
        escolher = int(input("Escolha um atributo para competir\n[1]Drible\n[2]Passe\n[3]Ritmo\n[4]Finalização\n[5]Físico\n[6]Defesa\nR: "))
      if escolher == 1:
        if self.drible > oponente.drible:
          print(f"{self.nome} ganhou de {oponente.nome} no atributo drible")
          
        elif self.drible == oponente.drible:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
        
        else: 
          print(f"{oponente.nome} ganhou de {self.nome} no atributo drible")
      
      if escolher == 2:
        if self.passe > oponente.passe:
          print(f"{self.nome} ganhou de {oponente.nome} no atributo passe")
        
        elif self.passe == oponente.passe:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
          
        else:
          print(f"{oponente.nome} ganhou de {self.nome} no atributo passe")
      if escolher == 3:
        if self.ritmo > oponente.ritmo:
           print(f"{self.nome} ganhou de {oponente.nome} no atributo ritmo")

        elif self.ritmo == oponente.ritmo:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
          
        else:
          print(f"{oponente.nome} ganhou de {self.nome} no aributo ritmo")
      if escolher == 4:
        if self.fina > oponente.fina:
          print(f"{self.nome} ganhou de {oponente.nome} no atributo finalização")

        elif self.fina == oponente.fina:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
          
        else:
           print(f"{oponente.nome} ganhou de {self.nome} no atributo finalização")
      if escolher == 5:
        if self.fisico > oponente.fisico:
           print(f"{self.nome} ganhou de {oponente.nome} no atributo físico")

        elif self.fisico == oponente.fisico:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
          
        else:
           print(f"{oponente.nome} ganhou de {self.nome} no atributo físico")
      if escolher == 6:
        if self.defesa > oponente.defesa:
           print(f"{self.nome} ganhou de {oponente.nome} no atributo defesa")
          
        elif self.defesa == oponente.defesa:
          print(f"{self.nome} empatou com o oponente {oponente.nome}")
          
        else:
           print(f"{oponente.nome} ganhou de {self.nome} no atributo defesa")