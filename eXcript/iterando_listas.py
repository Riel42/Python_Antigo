#=======================================================#
#====================Iterando Listas====================#
#=======================================================#

lista_nums = [100, 200, 300, 400]
for item in lista_nums: #signifca que a cada vez que for repetindo o código, será adicionado os valores da lista na variável item
    print (item)


lista2 = [10, 20, 30, 40, 50] #valores a serem adicionados
for item2 in range(0,5):
    lista2[item2] += 1000 # vai adicionar 1000 a cada elemento da lista2
print(lista2) #imprime o resultado

lista00 = [1,2,3,4,5]
for daqui in range (0,5):
    lista00[daqui] += 100 #variável daqui irá receber 100 e adicionar nos elementos da lista00
print(lista00)

