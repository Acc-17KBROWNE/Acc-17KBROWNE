import time
list0=[]
print(list0)

list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list1)
time.sleep(1)
list1[1] = 1
time.sleep(1)
list1[2]
time.sleep(1)
list1[-6]
time.sleep(1)
list1[7:10]
time.sleep(1)
list1[15:]
time.sleep(1)
del list1[1]
time.sleep(1)
list1.append(21)
time.sleep(1)
list1.extend(list0)
time.sleep(1)
list1.insert(27,19)
time.sleep(1)
list1.remove(4)
time.sleep(1)
list1.pop(5)
time.sleep(1)
list1.index(20)
time.sleep(1)
list1.count(8)
time.sleep(1)
list1.reverse()
time.sleep(1)
list1.copy()
time.sleep(1)
list1.clear()
time.sleep(1)
list1.sort()
print(list1)

time.sleep(1)

option=int(input("""1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list.
Please enter your choice (1-9):
 """))