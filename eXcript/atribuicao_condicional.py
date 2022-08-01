#============================================#
#===========Atribuição Condicional===========#
#============================================#

'''
Atribuição condicional é uma estrutura utilizada para
simplificar o código, onde o valor a ser atribuído
será aquele que satisfazer a condição.

<variável> = <valor1> if (True) else <valor2>
'''

x=int(input('Digite um número: '))
texto = 'Valor maior do que 50.' if x > 50 else 'Valor menor ou igual a 50.'
var = 'O valor é par.' if x % 2 == 0 else 'O valor é ímpar.'
print(texto, var)


