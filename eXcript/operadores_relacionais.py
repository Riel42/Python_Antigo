#============================================================#
#===================Operadores Relacionais===================#
#============================================================#

'''
(==) é o mesmo que igualdade
(!=) é o mesmo que diferente
(>)  é o mesmo que maior que
(<)  é o mesmo que menor que
(>=) é o mesmo que menor ou igual que
(<=) é o mesmo que maior ou igual que

VALORES BOOLEANOS
(True)  É O MESMO QUE VERDADEIRO
(False) É O MESMO QUE FALSO

(x == y) --> x é igual a y?
(x != y) --> x é diferente a y?
'''

print(100==100)
print('a'=='a')
print('b'=='a')
print(False==False)
print(False!=False)
print(True==1)
print(False==0)

print('')

a=(100!=100)
b=('a'=='a')
print(a,'\n',b)

print('')

print(5<5.1)
print(5<=5.1)

print('')

print((5<5.1) or (5==5.1))#se a primeira ou a segunda condição for verdadeira, então retorne verdadeiro.
print((5<5.1) and (5==5.1))#se a primeira condição e a segunda condição forem diferentes, retorne falso.
