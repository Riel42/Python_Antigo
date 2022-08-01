#==========================================================#
#===============Retorno de Valores Múltiplos===============#
#==========================================================#

'''
Retorno de Valores Múltiplos retornará
uma TUPLA!
'''

def func():
    return 1,2

a,b = func()

print(a, b)

#==========================================================#
print('\n')

tupla=(1,5)
c, d = tupla

print(c, d)

#==========================================================#
print('\n')

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado, cubo

q,c = potencia(10)
print('Quadrado: ',q,'\nCubo: ',c)
#==========================================================#
