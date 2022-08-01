#Utilização de tuplas

TUPLA = (1,2,3,4,5,6,7)

a,b,c,d,e,f,g = TUPLA

print (TUPLA)
print(b)
print(e+b)

'''
Dicionário é um conjunto de valores, onde cada valor é associado a uma chave de
acesso. Um dicionário em Python é declarado da seguinte forma:
Nome_dicionario = { chave1 : valor1,
chave2 : valor2,
chave3 : valor3,
......
chaveN : valorN}
'''
Dicionario={'arroz': 17.30, 'feijão':12.50,'carne':23.90,'alface':3.40}
print (Dicionario)
print (Dicionario['feijão'])

Dicionario ['carne'] = 10.50 #modificação do dicionário
print (Dicionario)

'''
Operações em dicionários

del --> Exclui um item informado a chave
in --> Verificar se uma chave existe no dicionário
keys() --> Obtém as chaves de um dicionário
values() --> Obtém os valores de um dicionário
'''
del Dicionario ['arroz']
print (Dicionario)
print('')
print('Batata' in Dicionario)#é como uma pergunta, tem a chave  batata no dicionário?
print('carne' in Dicionario)
print('')
print(Dicionario.keys())
print('')
print(Dicionario.values())

'''
7.2 Exercícios: dicionários

1 – Dada a tabela a seguir, crie um dicionário que a represente:

Salgado = R$ 4.50
Lanche = R$ 6.50
Suco = R$ 3.00
Refrigerante = R$ 3.50
Doce = R$ 1.00

2 – Considere um dicionário com 5 nomes de alunos e suas notas. Escreva um programa que calcule
a média dessas notas.

'''
tabela = {'Salgado R$' : 4.50, 'Lanche R$' : 6.50, '  Suco R$' : 3.00, 'Refrigerante R$' : 3.50, 'Doce R$' : 1.00}
print (tabela)

nota = {'Max' : 8.05, 'Josh' : 8.00, 'Calvin' : 6.00, 'Jeff' : 7.05, 'Chris' : 10.00}
print ((8.05 + 8.00 + 6.00 + 7.05 + 10.00)/5)

