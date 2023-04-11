from classejogador import Jogado
import random
import time
import os
#informática
#2 ano vespertino
#Programação Orientada a Objetos
#Alunos 
#Daniel Guimarães Souza 
#Danielly Vitória Ferreira da Costa 
#Luis Henrique Silva Botelho  
#Marcos Aurélio

#inicio -Daniel
print("Olá Você está jogando um jogo de super trunfo sobre o tema de futebol\nEspero que se divirta\n")

primeira_acao = int(input("Escolha uma opção.\n[1]Iniciar\n[2]Programadores\nR: "))
while primeira_acao != 1 and primeira_acao != 2 :
    print("Tente novamente")
    primeira_acao = int(input("Escolha uma opção.\n[1]Iniciar\n[2]Programadores\nR: "))
if primeira_acao == 1:
    loading = ("Carregando: {----------}")
    for i in range(11):
        os.system('cls')
        print (loading)
        print ("")
        loading = loading.replace("-","=",1)
        time.sleep(0.2)

if primeira_acao == 2:
    print('\033[1m'"="*15)
    print("Nossos programadores são:\nDaniel\nDanielly\nLuis\nMarcos")
    print("="*15,'\033[0;0m')
    time.sleep(4)
    os.system('cls')
    print("Vamos lá")


#criando os objetos 
Jogador1 = Jogado("Benzema","Masculino","Real Madrid",90,97,92,94,45,90)
Jogador2 = Jogado("Neymar","Masculino","PSG",87,87,90,95,39,64)
jogador3 = Jogado("Pelé","Masculino","Santos",93,96,96,96,60,76)
jogador4 = Jogado("Mbappé","Masculino","PSG",88,96,99,98,44,87)
jogador5 = Jogado("Formiga","Feminino","PSG",80,78,76,77,90,92)
jogador6 = Jogado("Marta","Feminino","Orlando Pride",90,89,85,96,34,70)
jogador7 = Jogado("Debinha","Feminino","Kansas City Current",93,88,85,87,50,77)

#lista cartas
lista_cartas = [Jogador1, Jogador2, jogador3, jogador4, jogador5, jogador6, jogador7]
#lista do usuário
carta_user = []
#lista da máquina
carta_maquina = []
#escolha da carta usuário -Daniel
os.system('cls')
escolher = int(input(f"Escolha de 1 a {len(lista_cartas)}\nR: "))
while escolher != 1 and escolher != 2 and escolher != 3 and escolher != 4 and escolher != 5 and escolher != 6 and escolher != 7:
  print("Tente novamente!")
  escolher = int(input(f"Escolha de 1 a {len(lista_cartas)}\nR: "))
escolher = random.randint(0, len(lista_cartas))
escolher -= 1
carta_user = lista_cartas[escolher]

#verificar qual carta foi escolhida e tirar da lista
if escolher == 0:
  lista_cartas.remove(Jogador1)
  print("Essa é sua carta escolhida")
  Jogador1.imprimir()
  

if escolher == 1: #neymar
  lista_cartas.remove(Jogador2)
  print("Essa é sua carta escolhida")
  Jogador2.imprimir()
if escolher == 2: #pelé
  lista_cartas.remove(jogador3)
  print("Essa é sua carta escolhida")
  jogador3.imprimir()

if escolher == 3: #mbappe
  lista_cartas.remove(jogador4)
  print("Essa é sua carta escolhida")
  jogador4.imprimir()


if escolher == 4: #formiga
  lista_cartas.remove(jogador5)
  print("Essa é sua carta escolhida")
  jogador5.imprimir()

if escolher == 5: #marta
  lista_cartas.remove(jogador6)
  print("Essa é sua carta escolhida")
  jogador6.imprimir()

if escolher == 6: #debinha
  lista_cartas.remove(jogador7)
  print("Essa é sua carta escolhida")
  jogador7.imprimir()
time.sleep(4)
os.system('cls')


#sorteio da máquina - Marcos

sorteado  = random.randint(0, len(lista_cartas))
sorteado -= 1
carta_maquina = lista_cartas[sorteado]

if sorteado == 0:
  print("Carta da máquina")
  Jogador1.imprimir()
  
if  sorteado == 1:
  print("Carta da máquina")
  Jogador2.imprimir()

if sorteado == 2:
  print("Carta da máquina")
  jogador3.imprimir()
  
if sorteado == 3:
  print("Carta da máquina")
  jogador4.imprimir()
  
if sorteado == 4:
  print("Carta da máquina")
  jogador5.imprimir()

if sorteado == 5:
  print("Carta da máquina")
  jogador6.imprimir()

if sorteado == 6:
  print("Carta da máquina")
  jogador7.imprimir()


#Comparação dos atributos Daniel e Marcos
time.sleep(4)
os.system('cls')
carta_user.compara(oponente=carta_maquina)

#competição Dani
time.sleep(4)
os.system('cls')
carta_user.definindo_ganhador(oponente= carta_maquina)
#finalzin legal
time.sleep(3)
loading = ("Desligando: {----------}")
for i in range(11):
  os.system('cls')
  print (loading)
  print ("")
  loading = loading.replace("-","=",1)
  time.sleep(0.2)


