#===============================================================#
#===================Exemplo com o operador IN===================#
#===============================================================#

a = 10
b = 25
c = 66

x = int(input('Digite um número: '))

if(x in [a,b,c]):
    print('Está contido.')
else:
    print('Não está contido.')

'''--------------------Outro Exemplo-----------------------'''

cores = ['Azul','Amarelo','Vermelho','Branco']

while True:
    valor = input('''Digite o nome de uma cor, para sair,
digite 0

''')

    if (valor=='0'):
        print('Fim da execução do programa ...')
        break
    if valor in cores:
        print('Cor contida!\n')
    else:
        print('Cor não contida!\n')

while True:
    print(100*'\nhehehe\n')
    break
    
