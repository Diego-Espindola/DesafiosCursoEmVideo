#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

menor_peso = 1000
maior_peso = 0

for c in range(0,5):

    nome = input('Informe o seu nome: ')
    peso = int(input('Informe o seu peso em quilos: '))
 

    if(peso < menor_peso):
        menor_peso = peso
        menor_nome = nome
    if(peso > maior_peso):
        maior_peso = peso
        maior_nome = nome

print(f'O maior peso foi do(a) {maior_nome}, pesando {maior_peso} kg\nO menor peso foi do(a) {menor_nome}, pesando {menor_peso} kg')