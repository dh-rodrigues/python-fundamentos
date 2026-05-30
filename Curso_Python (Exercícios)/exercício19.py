#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
aluno_1 = input('Qual o nome do primeiro aluno? ')
aluno_2 = input('Qual o nome do segundo aluno? ')
aluno_3 = input('Qual o nome do terceiro aluno? ')
aluno_4 = input('Qual o nome do quarto aluno? ')
escolha = [aluno_1,aluno_2,aluno_3,aluno_4]
print(random.choice(escolha))
