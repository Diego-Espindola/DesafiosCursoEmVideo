#Faça um programa que mostre na tela uma contagem regressiva
#para o estouro de fogos de artifício de 10 até 0
#com uma pausa de 1 segundo entre elas
#
from time import sleep

for contagem in range(11,0,-1):
    
    print(contagem-1)
    sleep(1)
print("💣")