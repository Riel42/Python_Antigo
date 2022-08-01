'''
Conteúdo da Aula - Estruturas de Repetição I: while

while vem do inglês que significa enquanto.

while é verdadeiro.

while alguma coisa:
    execute isso enquanto for versade

EXEMPLO:
'''
#Exemplo: programa que só para de aparecer valores quando ele chaga ao 101

n = 101
cont = 0
while cont < n:
    print (cont)
    cont = cont + 1

'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função potência da
linguagem.

2**3 = 1*2*2*2 = 8
'''
#O número do expoente indica o números de vezes que a base é multiplicada por
#ela mesma.
#A potência é o número 1 multiplicado pela a base o número do expoente vezes

base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valoe do expoente '))

cont = 0
produto = 1
while cont < expoente:
    produto = produto * base
    cont = cont + 1

print (base, 'elevado a', expoente, 'é igual a', produto)

'''
Dado um numero inteiro não-negativo n, determinar n! (valor fatorial)

Exemplo de fatorial:
3! = 3*2*1 = 6
'''
n = int(input('Digite o valor de n: '))

prod = n
cont = n - 1
while cont > 1:
    prod = prod*cont
    cont = cont - 1
print (n, '! igual a', prod)

'''
Dada uma sequência de números inteiros não-nulos,
seguida por 0, imprimir seus quadrados.
'''

num = int(input('Digite o primeiro número inteiro: '))
while num != 0:
    print (num,'ao quadrado vai ser igual a',num*num)
    num = int(input('Digite o próximo número: '))

