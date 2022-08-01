#========================================================================#
#====================Operadores Relacionais Compostos====================#
#========================================================================#

idade = int(input('Informe a sua idade: '))

if(idade <= 0):
    print('Idade inválida.')
elif(idade>150):
    print('Idade inválida.')
elif(idade<18):
    print('Você precisa ter uma idade maior que 18 anos para dirigir.')
else:
    print('Você pode dirigir.')
