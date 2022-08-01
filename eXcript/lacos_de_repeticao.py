#==================================================#
#================Laços de Repetição================#
#==================================================#

'''
While = enquanto

enquando(condição verdadeira):
    façaisso

While é semelhante ao if, mas o
if repete uma condição uma vez,
já o while repete aque instrução
até ela ser falsa. Se no caso o
while sempre for verdadeiro, o
seu programa não terá fim, o que
fará que ele trave e o usuário
terá de fechá-lo a força.
'''
#==============================#
#==========While-Else==========#
#==============================#

'''
While-Else é uma condição onde se
algo for verdadeiro ele executará tal
bloco de comando, se não, executará
outro bloco de comando, mas não
como um looping.
'''

x=0
while(x<11):
    print('Contagem: ',x)
    x += 1
else:
    print('O porgrama parou no número',x,'...')
print('Fim da execução ...')









