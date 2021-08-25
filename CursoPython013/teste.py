###Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while(True):
    numero += 1
    mult = 0

    for c in range(numero, 0, -1):
        if(numero%c == 0):
            mult += 1    
    if(mult==2):
        print(numero)
