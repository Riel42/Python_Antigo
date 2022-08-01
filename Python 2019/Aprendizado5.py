'''
Bibliotecas Python:

math: Funções matemáticas
time: Funções de tempo
smtplib: e-mail
tkinter: Interface Gráfica padrão

Bibliotecas externas de alto nível

urllib: Leitor de RSS para uso na internet
numpy: Funções matemáticas mais avançadas
PIL/Pillow: Manipulação de imagens
'''

import math
print(math.factorial(6))

'''
Resultados da pesquisa
Trecho da Web em destaque O fatorial de um número é calculado pela multiplicação
desse número por todos os seus antecessores até chegar ao número 1. No te que
nesses produtos, o zero (0) é excluído. O fatorial é representado por: n!
'''
'''
Sintaxe de IF:

if <condição> :
<Bloco de comandos >

Sintaxe de IF e ELSE:
if <condição> :
<Bloco de comandos para condição verdadeira>
else :
<Bloco de comandos para condição falsa>

Sintaxe de IF, ELIF E ELSE:
if <condição1> :
<Bloco de comandos 1>
elif <condição2> :
<Bloco de comandos 2>
elif <condição3> :
<Bloco de comandos 3>
:::::::::::::::::::::::::::::::::::::::::
else :
<Bloco de comandos default>

ATIVIDADES:

1 – Faça um programa que leia 2 notas de um aluno, calcule a média e imprima aprovado ou
reprovado (para ser aprovado a média deve ser no mínimo 6)

2 – Refaça o exercício 1, identificando o conceito aprovado (média superior a 6), exame (média
entre 4 e 6) ou reprovado (média inferior a 4).
'''
print ('')
print ('')
print ('')

NOTA = float(input('DIGITE A PRIMEIRA NOTA DO ALUNO: '))
NOTA2 = float(input('DIGITE A SEGUNDA NOTA DO ALUNO: '))

MEDIA = (NOTA + NOTA2)/2

if MEDIA >= 6:
    print ('O ALUNO FOI APROVADO!')
else:
    print ('O ALUNO FOI DESAPROVADO!')
   
print ('')
print ('')
print ('')

NOTA01 = float(input('DIGITE A PRIMEIRA NOTA DO ALUNO: '))
NOTA02 = float(input('DIGITE A SEGUNDA NOTA DO ALUNO: '))

MEDIA02 = (NOTA01 + NOTA02)/2

if MEDIA02 > 6:
    print ('O ALUNO FOI APROVADO!')

elif 4 < MEDIA02 < 6:
    print ('O ALUNO TERÁ DE PASSAR POR UM EXAME!')

elif MEDIA02 < 4:
    print ('O ALUNO FOI DESAPROVADO!')
    

