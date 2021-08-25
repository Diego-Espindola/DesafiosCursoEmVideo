###Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

def verificacao_primo(numero):
    mult = 0

    for c in range(numero, 0, -1):
        if(numero%c == 0):
            mult += 1


            
    if(mult==2):
        print(f'{numero} É um número primo')
    else:
        print(f'{numero} Não é um número primo')