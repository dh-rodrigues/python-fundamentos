#Pedir o ângulo e mostrar seno, cosseno e tangente
import math
angulo = float(input('Digite um ângulo para obter seu seno, cosseno e tangente: '))
seno = math.sin(math.radians(angulo))
print(f'O Seno de {angulo}° é {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O Cosseno de {angulo}° é {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'A Tangente de {angulo}° é {tangente:.2f}')