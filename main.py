from jogador import Jogado
import random
import time

#criando os objetos
benzema = Jogado("M", "Benzema", "Real", "França",90,97,92,94)
neymar = Jogado("M", "Neymar", "PSG", "Brasil",87,87,90,95)
pelé = Jogado("M", "Pelé", "Santos", "Brasil",96,96,99,76)
bappe = Jogado("M", "Mbappe", "PSG", "França",88,88,88,88)
formiga = Jogado("F","Formiga","PSG","Brasil",80,78,76,77)
Marta = Jogado("F","Marta","Orlando Pride","Brasil",90,89,85,96)
Debinha = Jogado("F","Debinha","Kansas City Current","Brasil",93,88,85,87)



#sorteio das cartas
lista_de_oponentes = ["benzema", "neymar", "pelé", "bappe","formiga","Marta","Debinha"]
sorteio  =  random.randint ( 0 , len( lista_de_oponentes ))
sorteio -= 1


#chamando as cartas
if sorteio == 0:
    print("Essa é sua carta 1:")
    benzema.imp()
if sorteio == 1:
    print("Essa é sua carta 1:")
    neymar.imp()
if sorteio == 2:
    print("Essa é sua carta 1:")
    pelé.imp()
if sorteio == 3:
    print("Essa é sua carta 1:")
    bappe.imp()
if sorteio == 4:
    print("Essa é sua carta 1:")
    formiga.imp()
if sorteio == 5:
    print("Essa é sua carta 1:")
    Marta.imp()
if sorteio == 6:
    print("Essa é sua carta 1:")
    Debinha.imp()

#sorteio da segunda carta
lista_de_oponentes2 = ["benzema", "neymar", "pelé", "bappe","formiga","Marta","Debinha"]
sorteio2  =  random.randint ( 0 , len( lista_de_oponentes2 ))
sorteio2 -= 1
#chamando as cartas
if sorteio2 == 0:
    print("Essa é sua carta 2:")
    benzema.imp()
    benzema.compara(oponente=sorteio)
if sorteio2 == 1:
    print("Essa é sua carta 2:")
    neymar.imp()
    neymar.compara(oponente=sorteio)
if sorteio2 == 2:
    print("Essa é sua carta 2:")
    pelé.imp()
    pelé.compara(oponente=sorteio)
if sorteio2 == 3:
    print("Essa é sua carta 2:")
    bappe.imp()
    bappe.compara(oponente=sorteio)
if sorteio2 == 4:
    print("Essa é sua carta 2:")
    formiga.imp()
    formiga.compara(oponente=sorteio)
if sorteio2 == 5:
    print("Essa é sua carta 2:")
    Marta.imp()
    Marta.compara(oponente=sorteio)
if sorteio2 == 6:
    print("Essa é sua carta 2:")
    Debinha.imp()
    Debinha.compara(oponente=sorteio)




















