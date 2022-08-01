'''
Laço for

Sintaxe:


for <variável> in range (início, limite, passo):
    <Bloco de comandos >

    ou
    
for <variável> in <lista> :
    <Bloco de comandos >

'''
#exemplo: sequência de 1 a 50 pulando de 5 em 5
Sequencia = 0
for soma in range (1,50,5):
    Sequencia = Sequencia + soma
    print (Sequencia)

#Soma das notas da lista

Lista_notas= [3.4,6.6,8,9,10,9.5,8.8,4.3]
soma=0
for nota in Lista_notas:
    soma = soma+nota
média = soma/len(Lista_notas)
print('Média = ', média)

