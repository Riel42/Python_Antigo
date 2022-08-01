#======================================================#
#==============Introdução aos Dicionários==============#
#======================================================#

'''
#================================================#
Dicionário: é um tipo de lista não ordenada
onde cada elemento está associado a uma chave.

OBS: No dicionário, não pode ter chaves iguais

Exemplo:
=======================
|CHAVE |      VALOR   |
=======================
| 'a'  | 'Péricles'   |
| 33.2 | 'Menelau'    |
|(1,2) | 'Atreu'      |
|'str' | 'Páris'      |
| 5    | 'Tiestes'    |
#================================================#
'''
dic = {} #criamos um dicionário
dic['aaa'] = 1000 #atribuímos um valor ao dicionário
dic['bbb'] = 2000
dic['ccc'] = 3000
dic['ddd'] = 4000
dic['eee'] = 5000
dic['fff'] = 6000
print(dic)
print(type(dic))

print(50*'=')

#Modo mais fácil de criar um dicionário:
dic2 = {1.1:'Olá', 3.5:True, 3.6: 5*'f'}
print(dic2)
