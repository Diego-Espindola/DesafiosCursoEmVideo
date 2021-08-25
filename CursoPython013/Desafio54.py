#Crie um programa que leia o ano de nascimento de sete pessoas.No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores, considere a maioridade 21 anos

total_pessoas = 0

for c in range(0, 7):
    idade = int(input('Informe a sua idade: '))
    if(idade>20):
        total_pessoas += 1

print(f'O total de pessoas que já atingiram a maior idade é {total_pessoas}')