def max():
    num1=int(input("Enter number: "))
    num2=int(input("Enter another number: "))
    if num1>num2:
        print(num1, "is the max")
    else:
        print(num2, "is the max")
max()

def multi2num():
    num3=int(input("Enter number: "))
    num4=int(input("Enter another number: "))
    print(num3*num4, "is the product of them")
multi2num()

def reversed():
    string1=str(input("Give me a string: "))
    list1=[]
    for ch in string1:
        list1.append(ch)
    list1.reverse()
    for i in range(list1):
        if i != " ":
            print(list1(i))
reversed()