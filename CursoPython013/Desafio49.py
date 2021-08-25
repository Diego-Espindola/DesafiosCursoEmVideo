###faça um for mostrando a tabuada de um número que o usuário escolher

numero_escolhido = int(input('Digite qual o número que você deseja saber a tabuada'))

for c in range(1, 11):
    print('{} * {} = {}'.format(numero_escolhido, c, numero_escolhido*c))
    