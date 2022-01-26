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
                if list1[j] > list1[j+1]:
                    num=list1[j]
                    list1[j]=list1[j+1]
                    list1[j+1]=num
        i= i+1
    print("Final List", list1)
    if dbg == True:
        print('Debug Info')
        print("BEFORE PASS %d: %s " %(i+1, list1)) 
        print("%s " %list1, end="-> ")  
        print("%s " %list1)
        print("AFTER PASS %d: %s " %(i+1, list1))     
    elif dbg == False:
        ('')
bubblesort(list1)

random.shuffle(list1)

def insertsort(list1, descending=False, dbg=False):
    marker=1
    print("Start list: ", list1)
    if descending==False:
        while (marker < len(list1)):
            j = marker
            while (list1[j] < list1[j-1] and j>0):
                temp = list1[j]
                list1[j] = list1[j-1]
                list1[j-1] = temp
                j = j-1
            marker = marker+1
    if descending==True:
        while (marker < len(list1)):
            j = marker
            while (list1[j] > list1[j-1] and j>0):
                temp = list1[j]
                list1[j] = list1[j-1]
                list1[j-1] = temp
                j = j-1
            marker = marker+1
    print("Sorted List: ", list1)
    if dbg == True:
        print('Debug Info')
        print("BEFORE PASS %d: %s " %(i+1, list1)) 
        print("%s " %list1, end="-> ")  
        print("%s " %list1)
        print("AFTER PASS %d: %s " %(i+1, list1))     
    elif dbg == False:
        ('')
insertsort(list1)

random.shuffle(list1)

def simpleselectsort(list1, descending=False, dbg=False):
    print(list1)
    marker = 0
    if descending==False:
        while marker < len(list1):
            index_of_min = marker
            for j in range(marker+1, len(list1)):
                if list1[index_of_min] > list1[j]:
                    index_of_min = j
            temp = list1[marker]
            list1[marker] = list1[index_of_min]
            list1[index_of_min] = temp
            marker = marker+1
        print(list1)
    if descending==True:
        while marker < len(list1):
            index_of_min = marker
            for j in range(marker+1, len(list1)):
                if list1[index_of_min] < list1[j]:
                    index_of_min = j
            temp = list1[marker]
            list1[marker] = list1[index_of_min]
            list1[index_of_min] = temp
            marker = marker+1
        print(list1)
    if dbg == True:
        print('Debug Info')
        print("BEFORE PASS %d: %s " %(i+1, list1)) 
        print("%s " %list1, end="-> ")  
        print("%s " %list1)
        print("AFTER PASS %d: %s " %(i+1, list1))     
    elif dbg == False:
        ('')
simpleselectsort(list1)