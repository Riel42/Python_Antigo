#============================================================#
#==============Lista - Quantidade de elementos ==============#
#============================================================#

'''
len = Quantidade, largura.

O len conta de 1 até x.
Mas, a lista conta de 0 até x.

Como a função len conta:

'Palavra','Palavra1','Palavra2'

   |1|  ,   |2|  ,    |3|

#---------------------------------------#

Como a list conta:

'Palavra', 'Palavra1', 'Palavra2'
   |0|         |1|         |2|
'''
lista = ['Abacaxi','Melão','Uva','Maracujá','Melancia','Limão']
print(len(lista))#Mostra quantos objetos eu tenho na minha lista.

print(lista[len(lista)-1])#Mostra o último elemento da lista, sendo que
                          #está contando de 1 até 7, mas já que a lista
                          #conta de 0 até x, então subtraímos 1.
lista.append('Mexerica')
lista.insert(2,'Mexerica')
print(lista)
print(lista.count('Mexerica'))#Count mostra quantas vezes um objeto aparece
                              #na lista.append

print(lista.index('Abacaxi'))#Mostrea o índice de tal objeto em uma lista.
