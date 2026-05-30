#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input("Digite seu nome completo: "))
print(f'Seu nome tem "Silva"?')
print(f'Analisando...')
print('SILVA' in nome.upper().strip())