#==================================================================================#
#====================Incluindo, alterando e excluindo elementos====================#
#==================================================================================#

lista = ['bbb','ccc','ddd']
lista.append('eee') #Adiciona 'eee' no final da nossa lista.
print(lista)
lista.insert(1, 'aletório')#Adiciona 'aleatório' na posição 1 (depois do 'bbb').
print(lista)
lista[2] = 'legal'#Altera uma posição desejada
print(lista[2])

lista.clear # Limpa uma lista.

lista = ['Banana', 2.5, 'Jeferson', True, 2*5, 'Azul']
lista.append('Batata')
lista.insert(2,'Mortadela')
lista.append(8.1)
lista.insert(3, 'Python!')
print(lista)
print(lista[0::2])

print(lista.pop(3))#exclui o elemento desejado(eu deletei o True).

del(lista[::2])#exclui os elementos saltando de 2 em 2.
print(lista)
