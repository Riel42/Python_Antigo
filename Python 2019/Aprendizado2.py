'''
Os quatro tipos numéricos simples, utilizados em Python, são números inteiros (int), números lon-
gos (long), números decimais (float) e números complexos (complex).

-----------------------------------------------------------------------------------------------------
ATIVIDADES:

1 – Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
z = (x**2 + y**2)/(x-y)**2

'''
print('Porgrama que recebe 2 números inteiros\n e resolve o seguinte problema:\n (x**2 + y**2)/(x-y)**2')
print('')
x = int(input('DIGITE O VALOR DE X: '))
y = int(input('DIGITE O VALOR DE Y: '))

z = (x**2 + y**2)/(x-y)**2
print(z)


