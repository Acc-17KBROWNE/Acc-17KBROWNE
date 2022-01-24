list1=[9,2,3,1,5,6,7,3,4,5]
print("Starting list: ", list1)
marker=1
exchange = True
n = len(list1)
i = 0

choice=int(input("1 for bubble sort, 2 for insert sort. What would you prefer? "))
if choice=1:
    while (i< n) and exchange:
        exchange=False
        for j in range(n-i-1):
            if list1[j] > list1[j+1]:
                num=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=num
                exchange = True
    print("Sorted List: ", list1)
if choice=2:
    while (marker < len(list1)):
        j = marker
        while (list1[j] < list1[j-1] and j>0):
            temp = list1[j]
            list1[j] = list1[j-1]
            list1[j-1] = temp
            j = j-1
        marker = marker+1
    print("Sorted List: ", list1)
else:
    print("no")