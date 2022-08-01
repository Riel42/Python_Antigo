'''
Aprendizado 1:

Novo sinal de comparação
<> (é igual ao !=)

Atividade 1:
Quanto é 2**(3+6) % 7?

Resposta: 1

type é uma função que retorna qual o tipo do objeto (inteiro, caracter ou real)
'''
print (2**(3+6)%7)

valor1 = 2
valor2 = 'Oi, mundo!'
valor3 = 3.5
print (type(valor1))
print (type(valor2))
print (type(valor3))

#int = integer (inteiro)
#str = string (caracteres)
#float = float (real)

'''
podemos fazer com que o programa mostre uma letra de uma palavra:
Exemplo:
'''
print('')
palavra = 'termodinâmica'
print (palavra[2]) 

'''
veja que apareceu o 'r', isso porque é a letra 2 da palavra termodinâmica.
É a letra 2 porque o computador também conta o 0

t = 0
e = 1
r = 2
m = 3
o = 4
d = 5
i = 6
n = 7
â = 8
m = 9
i = 10
c = 11
a = 12
'''
print('')
print(2*palavra[0])
'''Aqui eu fiz com que o programa fosse a letra 0 e fizesse que a letra 0
fosse multiplicada 2 vezes, e o resultado foi 'tt', muito bacana!
'''

'''
Eu também posso solicitar um intervalo de uma sequência. Por exemplo, para
solicitar os valores da sequência "palavra" que estão entre os endereços
9 e 12, fazemos:
'''
print('')
print(palavra [9:12])

'''
tabém podemos fazer do endereço (x) a diante, exemplo:
'''
print('')
print(palavra [9:]) #imprimiu mica, porque foi do endereço 9 a diante.

'''
também podemos fazer o contrário, veja:
'''
print('')
print(palavra[:9])
#ou
print(palavra[0:9])

#para a palavra toda
print('')
print(palavra[:])

#podemos colocar valores negativos para voltar para trás
print('')
print(palavra[7::-1])
print('')
print(palavra[7:0:-1])

print('')
palavra = palavra + ' aplicada'
print(palavra)
print(palavra[14:]) # o espaço conta como um caracter
print(len(palavra))#a função len mostra quantos caracteres tem uma palavra.

lista = [1,2,3]
print (lista)
print(lista[0])
print(lista[0] + lista[2])
lista[0] = 'zero'#não para fazer isso com strings
lista[1] = lista[2] 
print (lista)
lista[2] = lista[0] = lista[1]
print (lista)

