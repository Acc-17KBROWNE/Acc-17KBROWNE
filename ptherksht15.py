def cool(L):
    if len(L)==1:
        return L(0)
    else:
        print(sum(L))
L=[1, 2, 3, 4, 5, 6, 7]
cool(L)

def cool2(n):
    list1=[]
    if n==0:
        return 0
    else:
        for i in range(n%10):
            list1.append(n%10)
            n=n//10
    print(sum(list1))
cool2(1234567)