#==================================================#
#================Instrução Continue================#
#==================================================#

'''
Continue: A instrução continue interrompe
a execução de um único ciclo. Enquanto a
instrução break interrompe todos os
ciclos de um laço de repetição, a
instrução continue finaliza somente o
ciclo que está sendo executado.

exemplo:

for i in range(10):
    if (true):
        continue
    
'''
print('Início')
print()
i=0
while (i<10):
    i+=1
    if(i%2==0):
        continue
    print(i)
else:
    print()
    print('Saída da execução ...')
print('Fim da execução ...')

