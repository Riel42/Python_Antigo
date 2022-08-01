'''
No laço while, o trecho de código da repetição está associado a uma condição.
Enquanto a condição tiver valor verdadeiro, o trecho é executado. Quando a
condição passa a ter valor falso, a repetição termina.

Sintaxe:
while <condição> :
<Bloco de comandos>

senha = "54321"
leitura =" "
while (leitura != senha):
leitura = input("Digite a senha: ")
if leitura == senha :
print('Acesso liberado ')
else:
print('Senha incorreta. Tente novamente')

10.2 Laço for
O laço for é a estrutura de repetição mais utilizada em Python. Pode ser
utilizado com uma sequência numérica (gerada com o comando range) ou associado a
uma lista. O trecho de código da repetição é executado para cada valor da
sequência numérica ou da lista.

Sintaxe:

for <variável> in range (início, limite, passo):
<Bloco de comandos >

ou

for <variável> in <lista> :
<Bloco de comandos >



'''

