#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import os
# Define o caminho 
caminho_musica = r"C:\Users\Lenovo\OneDrive\Documentos\MeusProjetos\Ola Mundo\Curso_Python(Exercícios)\505.mp3"
os.system(f'start "" "{caminho_musica}"')