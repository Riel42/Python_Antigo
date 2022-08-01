'''
N = int(input()) 
X = int(input()) 
Y = int(input())
Z = int(input())

EvolucaoX = 0
EvolucaoY = 0
EvolucaoZ = 0

if 0 < N <= 1000: 
    if 1 <= X and Y and Z <= 1000:
        if X <= N:
            EvolucaoX += 1
        other = N - X
        if Y <= other:
            EvolucaoY += 1
        other1 = other - Y
        if Z <= other1:
            EvolucaoZ += 1

print(EvolucaoX+EvolucaoY+EvolucaoX)

#==========================================================#

X = int(input())
Z = list()
P = 1
result = 0

for i in range(3):

    P = int(input())
    Z.append(P)

Z.sort()

for i in range(3):
    
    if Z[i] <= X:
        result = result + 1
        X = X - Z[i]

print(result)'''

UpX = 0
UpY = 0
UpZ = 0


N = int(input())
if 0 <= N <= 1000:
    X = int(input())
    Y = int(input())
    Z = int(input())
    if 1 <= X <= 1000:
        if 1 <= Y <= 1000:
            if 1 <= Z <= 1000:
                if X <= N:
                    UpX = 1
                N = N - X
                if Y <= N:
                    UpY = 1
                N = N - Y
                if Z <= N:
                    UpZ = 1
                N = N - Z
            print(UpX + UpY + UpZ)
                
                    
        


























