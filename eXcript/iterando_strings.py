#========================================#
#============Iterando Strings============#
#========================================#

#EXEMPLO I

s = 'Iterando Strings'

for car in s:
    print(car)

print('\n')

#EXEMPLO II

s1 = 'Iterando Strings'
indice = 0

while indice < len(s):
    print(indice, s1[indice])
    indice += 1

print('\n')

#EXEMPLO III

for key, valor in enumerate('Iterando Strings'):
    print(key, valor)

print('\n')

#EXEMPLO VI
print(dict(enumerate('Iterando Strings')))

print('\n')
