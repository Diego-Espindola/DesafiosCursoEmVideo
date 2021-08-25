###Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro_termo = int(input('Insira o primeiro termo da progressão: '))
razao = int(input('Insira a razão da progressão: '))

quantidade_termos_progressao = 10
ultimo_termo = primeiro_termo+((quantidade_termos_progressao-1)*razao)


for c in range(primeiro_termo, ultimo_termo ,razao):
    print(c)