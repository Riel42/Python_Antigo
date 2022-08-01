#=====================================#
#================Break================#
#=====================================#

'''
Break: A instrução break
interrompe a execução do
laço de repetição onde
está contido.

exemplos:

for i in range(10):
    if(true):
        break
        
i = 10
while (i<100):
    i+=1
    if (true):
        break
'''

print('Entrada no laço:')
for item in range(100):
    print(item)
    if(item==50):
            break
print('Saída do laço.')

