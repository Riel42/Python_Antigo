'''
APRENDIZADO: MANIPULAÇÃO DE STRINGS

len() -> Retorna o tamanho da string.

capitalize() -> Retorna a string com a primeira letra maiúscula

count() -> Informa quantas vezes um caractere (ou uma sequência
de caracteres) aparece na string.

startswith() -> Verifica se uma string inicia com uma determinada
sequência.

endswith() -> Verifica se uma string termina com uma determinada
sequência.

isalnum() -> Verifica se a string possui algum conteúdo alfanu-
mérico (letra ou número).

isalpha() -> Verifica se a string possui apenas conteúdo alfabético.

islower() -> Verifica se todas as letras de uma string são minús-
culas.

isupper() -> Verifica se todas as letras de uma string são maiuscúluas.

lower() -> Retorna uma cópia da string trocando todas as letras
para minúsculo.

upper() -> Retorna uma cópia da string trocando todas as letras
para maiúsculo.

swapcase() -> Inverte o conteúdo da string (Minúsculo / Maiúsculo).

title() -> Converte para maiúsculo todas as primeiras letras de
cada palavra da string.

split() -> Transforma a string em uma lista, utilizando os espaços
como referência.

replace(S1,S2) -> Substitui na string o trecho S1 pelo trecho S2.

find() - > Retorna o índice da primeira ocorrência de um de-
terminado caractere na string. Se o caractere não
estiver na string retorna -1.

ljust() ->  Ajusta a string para um tamanho mínimo, acrescentando
espaços à direita se necessário.

rjust() -> Ajusta a string para um tamanho mínimo, acrescentando
espaços à esquerda se necessário.

center() -> Ajusta a string para um tamanho mínimo, acrescentando
espaços à esquerda e à direita, se necessário.

lstrip() -> Remove todos os espaços em branco do lado esquerdo
da string.

rstrip() -> Remove todos os espaços em branco do lado direito
da string.

strip() -> Remove todos os espaços em branco da string.


OBS: O número zero é importante! Ele é o primeiro número a
ser contado nas linguagens de programação.

EXEMPLO: Não é 1,2,3,4,5...
A órdem correta é: 0,1,2,3,4,5...

O ZERO É UM NÚMERO MUITO IMPORTANTE!

'''

teste = 'Apostila de Python'
print (len(teste))

a = "python"
print (a.capitalize())

b = "Linguagem Python"
print (b.count("n"))

c = "Python"
print (c.startswith("Py"))

d = "Python"
print (d.endswith("Py"))

e = "!@#$%"
print (e.isalnum())

f = "Python"
print (f.isalpha())

g = "pytHon"
print (g.islower())

h = "# PYTHON 12"
print (h.isupper())

i = "#PYTHON 3"
print (i.lower())

j = "Python"
print (j.upper())

k = "Python"
print (k.swapcase())

l = "apostila de python"
print (l.title())

m = "cana de açúcar"
print (m.split())

n = "Apostila teste"
print (n.replace("teste", "Python"))

o = "Python"
print (o.find("h"))

p = " Python"
print (p.ljust(15))

q = "Python"
print (q.rjust(15))

r = "Python"
print (r.center(10))

s = " Python "
print (s.lstrip())

t = " Python "
print (t.rstrip())

u = " Python "
print (u.strip())

'''
3.4 Exercícios: strings
1 – Considere a string A = "Um elefante incomoda muita gente". Que fatia
corresponde a "elefante incomoda"?
2 - Escreva um programa que solicite uma frase ao usuário e escreva a frase
toda em maiúscula e sem espaços em branco.

'''

'''PARTE 1'''

x = 'Um elefante incomoda muita gente'
print (x[0:20])
print ('')

'''PARTE 2'''


inp = str(input('Digite uma palavra.: '))

inp = inp.upper()
inp = inp.strip()
inp = inp.split()
print (inp)


'''CORREÇÃO:

EXERCÍCIO 2:'''

frase = input("Digite uma frase: ")
frase_sem_espaços = frase.replace(' ','')
frase_maiuscula = frase_sem_espaços.upper()
print(frase_maiuscula)


