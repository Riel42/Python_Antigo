'''
COMO MONTAR UMA LISTA:
'''

L = [2, 5, 'batata', 8, 3, (8+3)]
print (L)
print (L[0])
print (L[2])
print (L[2:])

L[5] = 'cenoura'
print (L[5])

H = [0,1,2,3,4,5]

print(len(H))
print(min(H))
print(max(H))
print(sum(H))
print(H.append (205))
print(H.extend([6,7,8]))
del H[1]
print(H)
print ([L+H])
print([L+H]*10)

print('')

K = list(range(5, 11))
print (K)
