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
list2=["a", "b", "c", "d"]
print(list2)
print("""1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list.""")
option=int(input("Enter a number from 1 to 9: "))

while option != 0:
    if option == 1:
        print("Option 1:")
        add=str(input("Enter an element to be appended to the list: "))           
        list2.append(add)
        print("The new list is ",list2)

    elif option ==2:
        print("Option 2:")
        enter=int(input("Insert an element to replace another element: "))
        replace=int(input("What do you want to replace? "))
        list2.insert(enter,replace)
        print(list2)
    
    elif option ==3:
        print("Option 3:")
        listo1=str(input("Enter a value: "))
        listo2=str(input("Enter another value: "))
        listo3=str(input("Enter another nother value: "))
        listo4=str(input("Enter another nother nother value: "))
        user_list=[listo1,listo2,listo3,listo4]
        list2.extend(user_list)
        print(list2)

    elif option ==4:
        print("Option 4")
        user_modify=int(input("What element would you want to modify: "))
        other_modify=str(input("What do you want to modify it to: "))
        list2[user_modify]=other_modify
        print(list2)

    elif option ==5:
        print("Option 5")
        list2.remove("d")
        print("The new list is:",list2)

    elif option ==6:
        print("Option 6")
        user_remove=str(input("Enter a element to remove: "))
        list2.remove(user_remove)
        print("The new list is: ",list2)

    elif option ==7:
        print("Option 7")
        list2.sort()
        print(list2)

    elif option ==8:
        print("Option 8")
        list2.sort(reverse=True)
        print(list2)

    elif option ==9:
        print("Option 9;")
        print("This is your current list",list2)
    
    else:
        print("ENTER A VALID NOMBRE BOZO")

    option2=int(input("If you wish to end enter 0, otherwise enter 1. If you wish to try that option again, enter any other number:"))
    if option2 ==0:
        break
    elif option2 ==1:
        option=int(input("""1. Append an element
2. Insert an element
3. Append a list to the given list
4. Modify an existing element
5. Delete an existing element from its position
6. Delete an existing element with a given value
7. Sort the list in the ascending order
8. Sort the list in descending order
9. Display the list.
Enter a number from 1 to 9: """))
    else:
        option = option
