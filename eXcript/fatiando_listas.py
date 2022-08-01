#=========================================#
#=============Fatiando Listas=============#
#=========================================#

'''
Slicing, do inglês, significa fatiar. Podemos
fazer cortes em uma lista a fim de obter uma
nova lista.

 0   1   2   3   4   5
|P| |Y| |T| |H| |O| |N|
-6  -5  -4  -3  -2  -1

lista [x:y:z]
       | | |
       | | |--> step
       | |
       | V
       |stop
       V 
    start

lista[começo:fim:intervalo]
'''
lista = 'Python'
print(lista[0:2])# De 0 até 2
print(lista[:2])#o mesmo anterior, de 0 até 2
print(lista[2:])#começa do 2 para frente
print(lista[::2])#Pulando um intervalo de 2 em 2.
print(lista[2::2])#começa do 2 e vai pulando de 2 em 2.
print(lista[::-1])#de trás para frente.
