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
    string1length=len(string1)
    reversedstring=string1[string1length::-1]
    print(reversedstring)
reversed()

def evennumber():
    list1=[]
    list2=[]
    things=int(input("How many numbers would u like to add to the list? "))
    for i in range(things):
        num=int(input("Enter number to list: "))
        list1.append(num)
    for i in range(len(list1)):
        if (list1[i])%2==0:
            list2.append(list1[i])
    print(list2)
evennumber()
