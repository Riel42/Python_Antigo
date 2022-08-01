#========================================#
#==============AND, OR & IN==============#
#========================================#

print(3 and 5 in range(0, 8))# de zero ao 8 é, na verdade, um range de 0 até 7. And: os dois tem que ser True para retornar True
print((3 or 10) in range(1, 8))#Or: se um dos objetos forem verdadeiros, o comando todo é verdadeiro
print((0 and 2) or (1 and 5) in range(1,9))#Retorna verdadeiro porque a segunda lista é verdadeira, fazendo todo o comando ser True.

#OBS: sempre o menor valor vai na frente no or, se não retornará False

print((10 or 2) in range(1,6))#retorna False

print((2 or 10) in range(1,6))#retorna True

'''
Isto ocorre porque o Python verifica só a primeira
expressão se for False, agora se retornar True, aí
sim ele verifica as outras expressões.

#-------------------------------------------------------#

print((10 or 2) in range(1,6))

Resultado: Por 10 não estar contido
no range de 1 até 6, o interpretador
simplesmente anula a verificação do
outro valor, e todo o comando da linha
vira False.
#-------------------------------------------------------#
print(((3 and 11) or (1 and 2)) in range(1, 8))

Resultado: Também retorna False, porque a primeira
expressão (3 & 11) é falsa, logo todo o comando fica
falso.
#-------------------------------------------------------#
'''
