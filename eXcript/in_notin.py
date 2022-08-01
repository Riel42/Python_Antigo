#=================================================#
#===================IN & NOT IN===================#
#=================================================#

'''
#====================================#
In = Contido em
Not In = Não contido em

x in [...] --> lista
x in (...) --> tupla
x in {...} --> dicionário
#====================================#
'''
tupla = (0,1,2,3,4,5,6,7,8,9,10)
print(2 in (tupla))# O valor 2 está na tupla? TRUE
print(11 in (tupla))# O valor 11 está na tupla? FALSE
print(11 not in (tupla))# O valor não 11 está na tupla? TRUE
print(11 not in range(1,12,))
print(11 in range(1,15,))
x = range(1,16)
if 5 in x:
    print('O valor está no range "x".')
else:
    print('O valor não está contido no range"x".')
