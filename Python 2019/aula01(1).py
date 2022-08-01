#Sintaxe mais fácil para o Python

ch = 'chaves'
print ('Utilize {} junto com o .format para substituir valores'.format(ch))

#o .format substitui as chaves por alguma variável ou valor

print ('Oi, {}!'.format('mundo'))
print ('O valor sucessor do 567 é o {}'.format(568))
var = 'chocolate'
print ('Eu {} de comer {}'.format('gosto', var))
print ('Muito obrigado, {}'.format('Guanabara'))
print ('Você é {}!'.format('10/10'))

var01 = float(input('Digite um valor: '))
var02 = float(input('Digite outro valor: '))
soma = var01 + var02
print ('a soma de {} e {} é igual a:'.format(var01, var02),soma)
