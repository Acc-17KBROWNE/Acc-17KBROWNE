import random
list1=[]
choice=int(input("How many would you like to add to the list? "))
for i in range(choice):
    number=int(input("Add to list: "))
    list1.append(number)
random.shuffle(list1)
def bubblesort(list1, descending=False, dbg=False):
    print("Starting list: ", list1)
    exchange = True
    n = len(list1)
    i = 0
    while (i< n) and exchange:
        exchange = False
        for j in range(n-i-1):
            if descending==False:
                if list1[j] > list1[j+1]:
                    num=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=num
                    exchange = True
            if descending==True:
                if list1[j] < list1[j+1]:
                    num=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=num
                    exchange = True
            if dbg == True:
                print('Debug Info')
                print("BEFORE PASS %d: %s " %(i+1, list1)) 
                print("%s " %list1, end="-> ")  
                print("%s " %list1)
                print("AFTER PASS %d: %s " %(i+1, list1))     
            elif dbg == False:
                ('')
        i= i+1
    print("Final List: ", list1)
bubblesort(list1)