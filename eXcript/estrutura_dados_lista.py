#============================================================#
#================Estruturas de Dados - Teoria================#
#============================================================#

'''
#=================================================#
Estruturas:
Estrutura de dados é qualquer
meio utilizado para armazenar
e recuperar informações.

#=================================================#
Lista: Sempre o último item vai embaixo

Norma da lista:

1. Novos itens sempre serão adicionados após o
último item

2. O primeiro item adicionado a lista
sempre será o primeiro elemento da lista.

Item 1
Item 2
Item 3
......
......
|     | <- Item X
#=================================================#
Pilha(Stack): Pilha é o conjunto de
objetos/elementos adicionados um
sobre o outro.

Norma geral:

1. o último a entrar será o último a sair.

2.O primeiro a entrar sempre será o último
elemento da lista

|    | <-- Item X
......
......
Item 4
Item 3
Item 2
Item 1

OBS: Imagine que a pilha é é como uma pilha de
livros, colocamos os livros de baixo para cima,
um em cima do outro, acumulados, é assim que
funciona a pilha.

#=================================================#
Array(Vetor): Array é uma estrutura de dados
estática para a manipulação de um número finito de
elementos de um mesmo tipo.

Array é constituído por um conjunto de elementos
finito e definido na sua declaração.

NORMA GERAL:

1. O índice zero é o primeiro elemento.

2.O índice do último elemento é o
"total_do_item1"

var[0] (3) -> índice = 0
var[1] (1) -> índice = 1
var[2] (9) -> índice = 2
var[3] (5) -> índice = 3
...
...
#=================================================#
Tupla: Estrutura semelhante a lista, mas é
imutável, não tem como alterá-la. Ela contém
de zero a 'n' elementos que não poderam serem
alterados.

Tupla é uma lista declarada como uma constante

NORMA GERAL:

1. Não é possível adicionar, remover, alterar
elementos.


2.Toda tupla será um conjunto de objetos, e
estes, também são imutáveis. Assim, se
adicionarmos o número 10 a posição 1, não
será possível atribuir ou alterar a posição
1.

tupla = (1, 2, 3)
print(tupla)

RESULTADO: (1, 2, 3)

#=================================================#
SET(Conjunto): Estrutura de dados semelhante a uma
lista. Um set tem como princípio conter uma lista 
de valores diferentes.

Set é uma lista sem itens repetidos

Item 1
Item 2
Item 3
Item 4
|    | <--X-- Item 4 (Tupla não repete valores.)

#=================================================#
Dicionário: Estrutura de dados onde cada elemento
está associado a uma chave que pode ser de
qualquer tipo.

Cada item do dicionário possui uma chave única.
Essa, é por definição diferente de todas as
outras.

| Chave | Valor |
 ---------------
| itemA |  568  |
| itemB |  878  |
| itemC |   15  |
| itemD |  100  |        ______________
                   <--- | itemE | 1000 |
                   
#=================================================#
Árvore: Estrutura de dados disposta numa
hierarquia. A estrutura de diretórios do nosso
computador é uma árvore.

NORMA GERAL:

1. Raiz: elemento pertencente ao nível um. Toda
árvore terá sempre uma única raíz.

2. Nó/Filho: Elemento que foi adicionado a outro
item.

3. Nível: propriedade que indicaquantos nós estão
acima de um filho.

*-------------------------------------------------*

Estrutura1 (Nível 0)
   |
   V
  Estrutura2 (Nível 1)
      |
      V
      Estrutura3 (Nível 2)
            |
            V
            Estrutura4 (Nível 3)
                   |
                   V
                   Estrutura5 (Nível 4)
                           |
                           V
                           Estrutura6 (Nível 5)
                           
#=================================================#                  
'''
 
