#=======================================================#
#=======================Lista III=======================#
#=======================================================#

lista = [1,2,3,4,5]
lista = [0] + lista +[6,7,8,9,10] #Adiciona na lista os elementos 6, 7 ,8, 9 e 10 no final e o elemento 0 no começo.
lista.append(11)#Outra forma de adicionar um elemento a uma lista.
print(lista)
del(lista[4])#exclue os elementos da lista.
print(lista)
print(10*[0])#cria 10 elementos de valor 0.
lista1 = [0,1,2,3,4,5]
lista1 += 10*[0] #somaremos a lista1 com 10 números 0
print(lista1)
print(50*'=') #imprime na tela cinquenta '='
