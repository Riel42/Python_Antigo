#A função input é que nem a função read do pascal, ou seja, ela lê o que o
#usuário escreve e guarda este valor


input ('Sua idade.: ')

#Podemos usar variáveis no imput


y = input ('Seu nome.:')
print ('Seu nome é.: ', y)

#A função int converte a simbolização do caracter para número

x = input ('Digite um valor.: ')
print (x)

#Vela que em x eu posso digitar qualquer coisa, se eu quiser só números, utilize
#a função int para converter as variáveis em números

x = int (x)

#Veja que quando eu digito uma letra quando pergunta "Digite um valor.:" dá erro,
#porque a função int está dizendo que x é um valor numérico, e não simbólico.


#Eu também posso fazer que na função imput podemos usar o int.

#Exemplo.:


num = int(input('Quantos animais você tem?' ))
print('Então você tem',num, 'animais.')

#Também podemos fazer operações matemáticas com esses valores.

var_1 = int(input('Digite o 1º Valor.: '))
var_2 = int(input('Digite o 2º Valor.: '))


print (var_1,'+',var_2,'igual a =', var_1+var_2)
print (var_1,'-',var_2,'igual a =', var_1-var_2)
print (var_1,'*',var_2,'igual a =', var_1*var_2)
print (var_1,'/',var_2,'igual a =', var_1/var_2)
print (var_1,'//',var_2,'igual a =', var_1//var_2)
print (var_1,'%',var_2,'igual a =', var_1%var_2)
print (var_1,'elevado a',var_2,'igual a =', var_1**var_2)
