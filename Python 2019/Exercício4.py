#Atividade 4

"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

ganha_hora = int(input('Quanto você ganha por hora?: '))
mes = int(input('Quantas horas você trabalha no mês? '))

x = ganha_hora*mes

print('Você ganha',x,'por mês!')
