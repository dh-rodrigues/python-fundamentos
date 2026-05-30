#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = input('Digite o nome de sua cidade: \n')
cidade = cidade.upper().strip()
print(cidade[:5] =="SANTO")