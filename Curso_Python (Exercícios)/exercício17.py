#Programa que lê a medida do cateto adjacente e oposto e mostra a medida da hipotenusa de um triângulo retângulo
import math
cateto_adjacente = float(input('Qual a medida do cateto adjacente? '))
cateto_oposto = float(input('Qual a medida do cateto oposto? '))
print('A medida da hipotenusa é = ' ,math.hypot(cateto_adjacente,cateto_oposto))