A = int(input())
B = int(input())

if A < B:
    B += 1
    while A != B:
        print(A, end=' ')
        A += 1
else:
    A += 1
    while B != A:
        print(B, end=' ')
        B += 1
    

