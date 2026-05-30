'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre: 
-O nome com todas as letras maiúsculas e minúsculas.
-Quantas letras ao todo (sem considerar espaços).
-Quantas letras tem o primeiro nome.'''

nome = input('Digite seu nome completo: '.strip())
print(nome.upper())
print(nome.lower())

total_sem_espaço = len(nome.replace(' ','')) 
print(total_sem_espaço)

primeiro_nome = nome.split()
print(len(primeiro_nome[0]))