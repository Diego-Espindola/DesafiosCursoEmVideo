###Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
soma_pares = 0
for c in range(0,6):
    if(c%2 == 0):
        soma_pares += c
print(soma_pares)