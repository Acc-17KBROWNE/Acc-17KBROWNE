def cool(L):
    if len(L)==1:
        return L(0)
    else:
        print(sum(L))
L=[1, 2, 3, 4, 5, 6, 7]
cool(L)

def cool2(n):
    if n<10:
        return n
    else:
        return n%10 + cool2(n//10)
print(cool2(1234567))
