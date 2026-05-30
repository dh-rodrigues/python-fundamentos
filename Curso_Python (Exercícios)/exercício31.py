#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância em KM da sua viagem?\n'))
viagem_curta = 0.50 * distancia
viagem_longa = 0.45 * distancia
if distancia <= 200 :
    print(f'O preço da sua passagem é R$ {viagem_curta:.2f}')
else:
    print(f'O preço da sua passagem é R$ {viagem_longa:.2f}')