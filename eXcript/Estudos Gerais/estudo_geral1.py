#============================================#
#==============ESTUDOS GERAIS I==============#
#============================================#

#========Imprimindo mensagem na tela========#
print('Oi, mundo!')

#========Lendo mensagem na tela========#
input('Qual o seu nome? ')

#========Criando Variáveis========#

a = 2
b = a*5
c = input('Qual a sua cor favorita? ')
print(c)
#========Imprimindo Variáveis========#

print(a,b)
print('2 elevado a 3+6 e tudo isto dividido por 7 ter o resto de: ',(2 ** (3+6)%7))

#========Vendo os tipos das variáveis========#
a1 = 'Hello, World!'
a2 = 2
a3 = 5.3

print(type(a1))
print(type(a2))
print(type(a3))

#========Manipulando Strings========#
print(a1[2::2])
print(a1[2:5])
print(a1[:5])
print(a1[7:])
print(a1[0:8:2])
print(a1[:])

#========Manipulando Strings de Trás para Frente========#

print(a1[10:5:-1])
print(a1[8:3:-1])
print(a1[7:2:-1])
print(a1[1:0:-1])
print(a1[2:0:-1])
print(a1[3:1:-1])
print(a1[10:3:-1])

#========Listas========#

lista1=[1,2,3,4,5]
lista2=['Suco',True,10*'=',1.5]
print(lista1, lista2)

#========Manipulando Listas========#

print(lista1[2]+lista1[3])
lista1 = lista1 + lista2
print(lista1)
print(lista1[::-1])
print(len(lista1))#mostra quantos elementos tem na lista
lista1[3] = 'Abacate'
print(lista1)

#========Criando Matrizes========#

lista_a = ['Legal',2,2.5]
lista_b = ['Maneiro',5,3.2]
lista_c = ['Genial',8,5*3]
matriz = [lista_a, lista_b, lista_c]
print(matriz)

#========Manipulando Matrizes========#

print(matriz[2][0])
print(matriz[1][2])
print(matriz[2][-1])#Mostra o último valor da lista_c

#========Tuplas========#

tupla = (1,2,'três',2*2,5*'=')
print(tupla)

#========Dicionários========#

clientes_senhas = {'fulano@email.com': '23j24h2io3', 'ciclano@email.com': '5h645i6o4', 'euclano@email.com':'k65h7ik567'}
print(clientes_senhas)
clientes_senhas['beltrano@gmail.com'] = '7iou867oi6'
print(clientes_senhas)

dicio = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
d = dicio.items() #transforma um dicionário em uma lista
print(d)
#========Concatenações========#
azul = 'Azul'
vermelho = 'Vermelho'
amarelo  = 'Amerelo'
numero = 6.52086867

print(azul +' '+ vermelho +' '+ amarelo)
print('Cores: %s'%azul,vermelho,amarelo)
print('Número igual a: %.3f'%numero)

#========Manipulando Listas II========#

lista_obj = [1, 'azul', 3*' Amarelo ',True, 'azul', 6.5]
print(lista_obj)
lista_obj.insert(0,'Começo')
lista_obj.append('Fim')
lista_obj.remove(6.5)
print(lista_obj)
print(lista_obj.count(True))

#========While========#

numero1 = 15
while numero1 != 0:
    print('Número:',numero1)
    numero1 -= 1

#========For========#

lista_for = ['Tieste', 'Menelau', 'Julia']
for i in lista_for:
    print(i)

for n in range(11):
    print(n)
    n += 1

#========Break========#

while 2 < 3:
    print(15*'=D\n'); break

#========If, Elif, Else========#

numeros_escolha = int(input('Digite um número e tecle enter: '))

if 0 <= numeros_escolha < 100:
    print('Valor positivo.')
elif 0 <= numeros_escolha > 100:
    print('Valor positivo grande.')
else:
    print('Valor negativo.')

#========Fim========#


