#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    km_acima = (velocidade - 8)*70
    print('A velocidade da via foi ultrapassa')
    print(f'Sua multa é de R$ {km_acima:.2f}')
else:
    print('Muito bem! Você está na velocidade permitida.')
    