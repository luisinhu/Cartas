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
sorteio = random.choice(lista_de_oponentes)
print("Esse será seu Oponente\n",sorteio)

sorteio2 = random.choice(lista_de_oponentes)
print("Esse será seu Oponente\n",sorteio2)























