#=======================================================================#
#=============Argumentos Nomeados vs Argumentos posicionais=============#
#=======================================================================#

'''
#=======================================================================#
Argumentos Nomeados = enviando um dicionário.
Argumentos posicionais = enviando uma tupla.

#=======================================================================#
'''
#ARGUMENTO POSICIONAL
def dados_pessoais(nome, sobrenome, idade, genero):
    print('Nome: {}\n Sobrenome: {}\nIdade: {}\nGênero: {}'
              .format(nome, sobrenome, idade, genero))

dados_pessoais(nome='Júlia',
               sobrenome='Almeida',
               idade=14,
               genero=True)#Gênero feminino = True,
                           #Gênero masculino = False.

print('\n')

#ARGUMENTO NOMEADO
def dados_pessoais2(nome2='Daniel', sobrenome2='Almeida', idade2='14', genero2=False):
    print('Nome: {}\n Sobrenome: {}\nIdade: {}\nGênero: {}'.format(nome2, sobrenome2, idade2, genero2)) 

dados_pessoais2()
