#============================================#
#==========PROPRIEDADES DAS STRINGS==========#
#============================================#

s = 'Lista de Caracteres'
print(len(s))
print(len('Isto tem vários caracteres :) !'))#mostra quantos caracteres tem esta frase
print(s[6])

print(s.split(' '))#quebra a frase em 3 partes, porque for retirado os espaços em branco.
lista = s.split(' ')
print(lista[0] + ' ' + lista[2])#Gambiarra para juntar de novo a palavra.
print(s.replace('Caracteres', 'Batatas'))#Substitui a palavra 'Caracteres' por 'Batatas'
