"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if

EXEMPLO:

area = int(input("Digite a área a ser pintada: "))

litros = area//3
if area % 3 > 0:
    litros = litros + 1

latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Você precisara de", latas, "latas.")
print("Você vai pagar R$", latas*80)

"""
area = int(input('Digite quantos metros quadrados da área a ser pintada.: '))
litros = area//6

if area % 6 > 0:
    litros = litros + 1

latas = litros//18
galoes = litros//4
mistura = litros//22


if litros % 18 > 0:
    latas = latas + 1
    print ('Você precisa de',latas,'lata/s.')
    print ('O preço é.:',latas*80)

    if litros % 4 > 0:
        galoes = galoes + 1
        print ('Você precisa de',galoes,'galão/s.')
        print ('O preço é.:',galoes*25)
        
if litros % 22 > 0:
    mistura = mistura + 1
    print ('Você precisa de',mistura,'da latão.')
    print ('O preço é.:',(mistura*105)//10)


























