#==================================================#
#================Comparando Strings================#
#==================================================#

'''
Atabela ASCII é a conversão de valores decimais e
binários de cada caracter. Assim, podemos saber
se tal letra, número, caracter especial é maior
ou menor que outro.

O comando ord mostra o valor de tal caracter.
O comando chr mostra o caracter que representa tal valor. 

Veja o exemplo a seguir:
'''
print('a' > 'X')
print('x' > 'a')
print('b' > 'D')
print('a' > '2')
print('a' > '3')
print('b' > '#')

print(ord('!'))
print(chr(300))

for c in range(800):
    print(chr(c))
