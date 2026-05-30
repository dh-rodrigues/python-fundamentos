#Programa que receba a largura e altura de uma parede em metros, calcule a aréa da parede e quantidade de tinta necessária para pinta-lá, considerar que cada litro de tinta pinta uma área de 2 m²
l = float(input('Qual a largura da parede em metros?'))
h = float(input('Qual a altura da parede em metros?'))
a = l*h
print('Para pintar uma parede com área {}m², será necessário {} litros de tinta'.format(a,a/2))