"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

valor = int(input('Escreva um valor menor que 1000: '))
valor01 = 'Unidade'
valor02 = 'Unidades'
valor03 = 'Dezena'
valor04 = 'Dezenas'
valor05 = 'Centena'
valor06 = 'Centenas'

if valor == 1:
    print(valor, valor01)

if 9 > valor > 1:
    num = valor // 1
    num1 = valor % 1
    print (num, valor02)

#SOLUÇÃO PERFEITA!
if 20 > valor >= 11:
    num = valor // 10
    num1 = valor % 10
    print (num, valor03,'e',num1, valor02 )

if 30 > valor > 20:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 40 > valor > 30:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 50 > valor > 40:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 60 > valor > 50:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 70 > valor > 60:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 80 > valor > 70:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 90 > valor > 80:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if 100 > valor > 90:
    num = valor // 10
    num1 = valor % 10
    print (num, valor04,'e',num1, valor02 )

if valor == 100:
    num2 = valor // 100
    print (num2, valor05)

#GENIAL!
if 200 > valor > 100:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 300 > valor > 200:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 400 > valor > 300:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 500 > valor > 400:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 600 > valor >= 500:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 700 > valor > 600:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 800 > valor > 700:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 900 > valor > 800:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if 999 > valor > 900:
    num2 = valor // 100
    num3 = (valor % 100) // 10
    var = valor % 10
    print (num2, valor06,',',num3, valor04, 'e' , var ,valor02)

if valor == 100:
    hehehe = 100 // 100
    print (hehehe, valor06)

if valor == 200:
    hehehe = 200 // 100
    print (hehehe, valor06)

if valor == 300:
    hehehe = 300 // 100
    print (hehehe, valor06)

if valor == 400:
    hehehe = 400 // 100
    print (hehehe, valor06)

if valor == 500:
    hehehe = 500 // 100
    print (hehehe, valor06)

if valor == 600:
    hehehe = 300 // 100
    print (hehehe, valor06)

if valor == 700:
    hehehe = 300 // 100
    print (hehehe, valor06)

if valor == 800:
    hehehe = 800 // 100
    print (hehehe, valor06)

if valor == 900:
    hehehe = 900 // 100
    print (hehehe, valor06)

if valor == 20:
    hehehe = 20 // 10
    print (hehehe, valor06)

if valor == 30:
    hehehe = 30 // 10
    print (hehehe, valor06)

if valor == 40:
    hehehe = 40 // 10
    print (hehehe, valor06)

if valor == 50:
    hehehe = 50 // 10
    print (hehehe, valor06)

if valor == 60:
    hehehe = 60 // 10
    print (hehehe, valor06)

if valor == 70:
    hehehe = 70 // 10
    print (hehehe, valor06)

if valor == 80:
    hehehe = 80 // 10
    print (hehehe, valor06)

if valor == 90:
    hehehe = 90 // 10
    print (hehehe, valor06)





if valor >= 1000:
    print('VALOR INVÁLIDO!')


#ESTÁ QUASE PERFEITO! SÓ FALTA ALGUNS AJUSTES...





    


    
    


 
    

















