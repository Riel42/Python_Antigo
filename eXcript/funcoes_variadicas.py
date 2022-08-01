#===============================================#
#==============Funções: Variádicas==============#
#==================Última Aula==================#
#==============Obrigado, eXcript!!==============#
#===============================================#

'''
Função Variádica: é toda função  capaz
de receber quantidades arbitrárias de
parâmetros.

(*args) = Lista.
(**kwargs) = Dicionário.
'''

def lista_de_argumentos(*lista): #O asterístico faz com que a variável lista consiga receber vários valores.
    print(lista)

lista_de_argumentos(1,2,3,4,5,6)
lista_de_argumentos('Azul','Roxo','Cinza','Bege','Preto','Branco')

def lista_arg_associativos(**dicionario):
    print(dicionario)

lista_arg_associativos(a=1, b=3, c=True, d='Olá!', e=5*'=')

def arg(*args, **kwargs):
    print(args, kwargs)

arg(1,2,3,4,5, um = '01', dois = '02', tres = '03')

