#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import calendar
ano = int(input('Digite um ano para verificar se este ano e bissexto:\n'))
if calendar.isleap(ano) == True:
    print(f'O ano de {ano} é um ano bissexto')
else:
    print(f'O ano de {ano} não é um ano bissexto')