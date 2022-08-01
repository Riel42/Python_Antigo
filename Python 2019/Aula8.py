"""
Nesta aula eu vou aprender sobre   Estrutura de Decisões.

Voltando ao programa que você tem que digitar um valor maior ou igual a 10
para receber true, senão receberá false
"""


val = int(input('Digite um valor maior ou igual a 10.: '))
x = (val >= 10)
print(x)

print('')
#Mas vamos usar as  Estrutura de Decisões para dar uma resposta determinada, não
#um valor booleano

#if é o mesmo que 'se', e else é o mesmo que 'senão'

val2 = int(input('Digite um valor maior ou igual a 10.: '))
x = (val2 >= 10)
#Primeiro Bloco

if x == True:
    print ('Você digitou um valor maior ou igual a 10, parabéns!')
#Segundo Bloco
    
if x == False:
    print ('Você digitou um valor menor que 10, você errou!')

"""
Outra forma de escrever o mesmo código:

val2 = int(input('Digite um valor maior ou igual a 10.: '))
x = (val2 >= 10)

if x:
    print ('Você digitou um valor maior ou igual a 10, parabéns!')

if x != True:
    print ('Você digitou um valor menor que 10, você errou!')

E tem como modificar mais vezes, se quiser mais detalhes, assista novamente a
aula "Aulas Python - 009 - Estrutura de Decisões I: if e else", de  Ignorância
Zero.
"""

val3 = int(input('Digite um valor maior ou igual a 10.: '))
x = (val3 >= 10)

if x == True:
    print ('Você digitou um valor maior ou igual a 10, parabéns!')

if x == False:
    print ('Você digitou um valor menor que 10, você errou!')

if val3 >= 100:
    print ('Você digitou um valor maior que 100, merece um cookie virtual ')

"""    
Como você pode perceber, quando eu digito um valor maior que 100, aparece duas
mensagens, aparece a de maior que 10 e ao mesmo tempo a de maior que 100, isso
ocorre porque ele lê todo o código, então ao mesmo tempo que ele leu o
primeiro bloco, ele também leu o segundo e o terceiro bloco, e utilizou
o primeiro e o terceiro.

Eu também poderia ter feito isso:
if x == True:
    print ('Você digitou um valor maior ou igual a 10, parabéns!')
    if val3 >= 100:
        print ('Você digitou um valor maior que 100, merece um cookie virtual')
        
if x == False:
    print ('Você digitou um valor menor que 10, você errou!')


Ou seja, eu posso colocar um bloco dentro de outro bloco relacionado.
"""

#Vamos fazer outro programa, só que utilizando uma codificação mais simples

var = int(input('Digite um valor maior que 200.: '))

if var >= 200:
    print ('Parabéns, você digitou um valor maior ou igual a 200')
else:
    print ('Você não escreveu o valor desejado, tente novamente.')

"""
O else, como escrito anteriormente, ele serve para "senão", e é isso que ele
executou, ele executou a mensagem para o else.
"""

    


    
