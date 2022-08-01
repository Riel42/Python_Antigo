#============================================#
#==============Fatiando Strings==============#
#============================================#

'''
Para o Python, toda string é uma lista imutável.

Revisão:

lista[começo:fim:intervalo]

Exemplo:

fulano = 'Fulano'
print(fulano[2::2]) #Começa do ponto 2 e tem um intervalo (ir pulando) de 2 em 2

Resultado: ln
'''
text = ('Texto legal!')
print(text[0])
print(text[0-1])#Retorna o último caracter.
print(type(text[0]))#No caso, cada caracter representa uma string no Python.
print(text[2::2])
print(text[2:8:1])
print(text[::-1])
print(text[::3])



