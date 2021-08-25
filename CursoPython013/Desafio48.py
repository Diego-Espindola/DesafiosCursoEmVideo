#Faça um programa que calcule 
# a soma entre todos os números ímpares que 
# são múltiplos de 3 e que se encontram entre 1 e 500
soma_impar = 0
for contador in range(1,501):
    if(contador%3==0):
        soma_impar += contador
print(soma_impar)