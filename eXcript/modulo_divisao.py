#=============================================================#
#======================Módulo da Divisão======================#
#=============================================================#

#Módulo da Divisão = resto da divisão

print(10%5)#Resto da divisão 10/5. Utilizamos o sinal de %.
print(5%2)
print(3%2.8)

print('\n')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

divisao = num1 / num2
resto = num1 % num2
print('\n')
print(num1, 'dividido por', num2,'é igual a: %.2f' %divisao)
print('Resto da divisão de', num1,'e',num2,'é igual a: %.2f' %resto)
