from jogador import Jogado
import random
import time

#criando os objetos
benzema = Jogado("M", "Benzema", "Real", "França",90,97,92,94)
neymar = Jogado("M", "Neymar", "PSG", "Brasil",87,87,90,95)
pelé = Jogado("M", "Pelé", "Santos", "Brasil",96,96,99,76)
bappe = Jogado("M", "Bappe", "PSG", "França",88,88,88,88)
formiga = Jogado("F","Formiga","PSG","Brasil",80,78,76,77)
Marta = Jogado("F","Marta","Orlando Pride","Brasil",90,89,85,96)
Debinha = Jogado("F","Debinha","Kansas City Current","Brasil",93,88,85,87)



#sorteio das cartas
lista_de_oponentes = ["benzema", "neymar", "pelé", "bappe","formiga","Marta","Debinha"]
sorteio  =  random.randint ( 0 , len ( lista_de_oponentes ))
sorteio  -=  1
print ( lista_de_oponentes [ sorteio ])
#chamando a carta
if sorteio == 0:
    print("Esse será seu oponente 1:\n")
    benzema.imp()
if sorteio == 1:
    print("Esse será seu oponente 1:\n")
    neymar.imp()
if sorteio == 2:
    print("Esse será seu oponente 1:\n")
    pelé.imp()
if sorteio == 3:
    print("Esse será seu oponente 1:\n")
    bappe.imp()
if sorteio == 4:
    print("Esse será seu oponente 1:\n")
    formiga.imp()
if sorteio == 5:
    print("Esse será seu oponente 1:\n")
    Marta.imp()
if sorteio == 6:
    print("Esse será seu oponente 1:\n")
    Debinha.imp()



lista_de_oponentes2 = ["benzema", "neymar", "pelé", "bappe","formiga","Marta","Debinha"]
sorteio2 =  random.randint ( 0 , len ( lista_de_oponentes2 ))
sorteio2  -=  1
print ( lista_de_oponentes2 [ sorteio2 ])
#chamando a carta
if sorteio2 == 0:
    print("Esse será seu oponente 2:\n")
    benzema.imp()
if sorteio2 == 1:
    print("Esse será seu oponente 2:\n")
    neymar.imp()
if sorteio2 == 2:
    print("Esse será seu oponente 2:\n")
    pelé.imp()
if sorteio2 == 3:
    print("Esse será seu oponente 2:\n")
    bappe.imp()
if sorteio2 == 4:
    print("Esse será seu oponente 2:\n")
    formiga.imp()
if sorteio2 == 5:
    print("Esse será seu oponente 2:\n")
    Marta.imp()
if sorteio2 == 6:
    print("Esse será seu oponente 2:\n")
    Debinha.imp()        






















