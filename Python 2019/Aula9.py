"""
Nessa aula eu vou aprender sobre Comparações Múltiplas

Nessa aula, criaremos um programa onde pessoas de 18 a 70 anos de idade
ganharam um benefício.
"""

idade = int(input('Digite sua idade.: '))

if idade >= 18:
    if idade < 70:
        print ('Você pode receber o benefício')
    else:
        print ('Você não pode receber o benefício')
else:
    print ('Você não pode receber o benefício')

"""
A podemos usar mais de uma comparação ao mesmo tempo
"""
print ('')
n = 3

print (1 < n < 5)

"""
Como podemos ver, o programa devolveu true porque 1 é menor que 'n' e 'n'
é menor que 5.

o = 3
"""

print ('')
print (1 < n < 2)

"""
Veja que o programa devolveu false, porque 'n' não é menor que 2, mesmo 1
sendo menor que 'n', sempre a programação dará preferência ao false.
"""
print ('')
print (1 < n > 4)
print (1 <= n < 5)
print(3 <= 3 <= 3)
print (3 == 3 < 5)

"""
Vela que bacana que ocorre agora
"""
print ('')
print ((1 < 3) <2)

"""
Primeiro ele compara se 1 é menor que 3, que dá True, e depois ele compara se
True é menor que 2, que dá True, porque True representa o valor 1, e False
representa o valor 0!
"""
print ('')
print (1 < 3 < 5 < 7 < 9 < 10)

"""
Também podemos comparar vários números de cada vez!
"""
print (1 < 3 < 5 < 7 < 9 < 10 < 5)
"""
O problema é que, mesmo tendo mais condições verdadeiras, sempre se tiver
uma condição falsa, ele devolve False, no caso ele devolveu False porque
10 é menor que 5.
"""

"""
Agora que sabemos comparações múltiplas, vamos voltar ao código do início:
"""

idade = int(input('Digite sua idade.: '))

if 18 <= idade < 70:
    print ('Você pode receber o benefício')
else:
    print ('Você não pode receber o benefício')
