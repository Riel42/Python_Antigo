#==================================================
#==========Características das Variáveis===========
#==================================================

'''
Características das Variáveis:

1. Elas possuem um nome.
2. Elas possuem um tipo.
3. Elas possuem um tamanho.
4. Elas possuem um valor.

 ______        _______
| NOME | <--- | VALOR |
 ^^^^^^        ^^^^^^^

Nome da       Valor a ser              
variável       atribuído

Recomendações e regras para criar variáveis:

1. Deixe ela com o nome todo minúsculo;
2. Não pode ter um número na frente da variável;
3. Não dê um nome reservado para a variável (como float, string, True, etc);
4. Só utilize underline como caracter especial. Arroba, hashtag entre outros não é recomendado;
5. Não dê espaço na variável, utilize underline;
6. Não utilize acentos;
7. Não usar as letras I e O;
8. Use variáveis com nomes pequenos.

exemplos:

Correto: variavel, var_01, Minha_variavel.
Errado:  variável, 1var, var 1, print, VaRiÁvEl, v@ri-a!vel, I, O, etc.

Constantes:

Utilize as mesmas regras das variáveis, mas com o nome todo maiúsculo e evite usar números.

Certo: CONSTANTE_EXEMPLO.
Errado: variável, 1var, var 1, print, VaRiÁvEl, v@ri-a!vel, I, O, etc. 
'''
nome_variavel = 20  #tipo inteira
var01 = 12.05       #tipo float
print(type(nome_variavel))
print(type(var01))
