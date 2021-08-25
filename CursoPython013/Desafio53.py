#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#print('**********************************************************')
#print('Este programa descobre se a frase digitada é um palíndromo')
#print('**********************************************************')

#frase = input('Digite a frase: ').replace(" ", "")

def teste_palindromo(frase):
        
    frase = (frase.replace(" ", "")).lower()

    frase_invertida = ''

    for c in frase[::-1]:
        print(c)
        frase_invertida += c

    if(frase == frase_invertida):
        print('Essa frase é um palíndromo')
    else:
        print('Essa frase não é um palíndromo')