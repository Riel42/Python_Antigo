'''
Nessa aula eu aprendi a biblioteca Math

funções dessa biblioteca:

ceil: arredonda para cima
floor: arredonda para baixo
trunc: elimina a vírgula para frente
pow: potenciação (ou **)
sqrt: raíz quadrada
factorial: fatorial de um valor (ou n!)

IMPORTAÇÃO DA BIBLIOTACA MATH:

import math

from math import (a função que eu quero)
exemplo:
from math import ceil

ou

import math
'''

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print ('A raíz quadrada de {} é igual a {}' .format(num, math.trunc(raiz)))
print ('Em valor real, a raíz quadrada de {} é igual a {:.5f}' .format(num, raiz)) #o :.(número)f seve para mostrar quantos números eu quero depois da vírgula

print('')
import random #biblioteca para valores aleatórios
var = random.random() #aqui ele escolherá um valor de 0 até 1
print(var)

val = random.randint(1, 100)#aqui ele escolherá um número aleatório de 1 a 100
print(val)
