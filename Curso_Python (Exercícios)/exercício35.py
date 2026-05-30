#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta_1 = float(input('Digite o valor do primeiro segmento: '))
reta_2 = float(input('Digite o valor do segundo segmento: '))
reta_3 = float(input('Digite o valor do terceiro segmento: '))
 
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Um triângulo pode ser formado a partir das informações apresentadas')
else:
    print('Um triângulo não pode ser formado a partir das informações apresentadas')

