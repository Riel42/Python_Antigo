#==================================================#
#==============Funções de Dicionários==============#
#==================================================#

tel = {36548934: 'Péricles', 36548534: 'Menelau', 32548934: 'Atreu', 36848934: 'Tieste'}
del(tel[36548534])
print(tel)
print(len(tel))
print(tel.keys())#Retorna as chaves do dicionário.
print(tel.values())#Retorna os valores do dicionário.
print(tel.get(36848934))#Retorna o valor relacionado a chave.
print(tel.popitem()) #Remove um elemento.
print(tel)
tel = {36548934: 'Péricles', 36548534: 'Menelau', 32548934: 'Atreu', 36848934: 'Tieste'}
print(tel)
print (35234534 in tel)
print (36548534 in tel)
tel2 = {547456721: 'Fulano', 547556721:'Ciclano' ,546456721:'Euclano' ,577456721:'Beltrano'}
tel.update(tel2)#mescla tel com tel2.
print(tel)
tupla = (10,20,30,30,20)
tel[tupla] = 'Cubo de Rubik'
print(tel)
