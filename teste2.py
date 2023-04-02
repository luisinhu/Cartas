from teste import Jogado
import random
import time


benzema = Jogado("M", "Benzema", "Real", "França",90,97,92,94)
neymar = Jogado("M", "Neymar", "PSG", "Brasil",87,87,90,95)
pelé = Jogado("M", "Pelé", "Santos", "Brasil",96,96,99,76)
bappe = Jogado("M", "Bappe", "PSG", "França",88,88,88,88)




lista_de_oponentes = ["benzema", "neymar", "pelé", "bappe"]
sorteio2 = random.randint(0, len(lista_de_oponentes))
sorteio2 -= 1
print(lista_de_oponentes[sorteio2])
if sorteio2 == 0:
    print("Esse será seu Oponente\n")
    benzema.imp()
elif sorteio2 == 1:
    neymar.imp()

elif sorteio2 == 2:
    pelé.imp()
elif sorteio2 == 3:
    bappe.imp()


time.sleep(5)


lista_de_jogadores = ["Benzema", "Neymar", "Pelé","Bappe"]
sorteio = random.randint(0, 4(lista_de_jogadores))
sorteio -= 1
print(lista_de_jogadores[sorteio])
if sorteio == 0:
    print("Esse será seu Jogador\n")
   
    benzema.imp()
    benzema.compara(sorteio2)
elif sorteio == 1:
    neymar.imp()
    neymar.compara(sorteio2)
elif sorteio == 2:
    pelé.imp()
    pelé.compara(sorteio2)
    
elif sorteio == 3:
    bappe.imp()
    bappe.compara(sorteio2)


















