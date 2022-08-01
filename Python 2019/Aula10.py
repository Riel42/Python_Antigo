'''
Nesta aula eu vou aprender Estrutura de Decisões II: if, elif e else.

Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor
inválido.
'''

dia = int(input("Digite o dia da semana: "))


if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
    verifica = True
else:
    print ('ENTRADA INVÁLIDA!')

'''
elif => Verifica se essa condição é verdadeira, senão, ele verifica a pŕxima
condição.
'''

'''
FAÇA UM PROGRAMA QUE LEIA 3 NÚMEROS E MOSTRE-OS EM ORDEM DECRESCENTE.
'''

a = int(input('DIGITE O PRIMEIRO NÚMERO: '))
b = int(input('DIGITE O SEGUNDO NÚMERO: '))
c = int(input('DIGITE O TERCEIRO NÚMERO: '))

if a >= b >= c:
    print(a, b, c)
elif a >= c >= b:
    print(a, c, b)
elif b >= a >= c:
    print(b, a, c)
elif b >= c >= a:
    print(b, c, a)
elif c >= a >= b:
    print(c, a, b)
else:
    print(c, b, a)

