# Question 16(a)
# Name and School: Kevin Browne, Athlone Community College

import random
test=str
a="You are now enrolled in the trial to recieve Super vaccine A"
b="You are now enrolled in the trial to recieve Super vaccine B"
c="You are now enrolled in the trial to recieve Super vaccine C"
choices=[a, b, c]
while test!="END":
    s_name=input("Enter your surname:      ")
    f_name=input("Enter your first name:      ")
    age=int(input("Enter your age:      "))
    eircode=str(input("Enter your Eircode:      "))
    trial=str(input("""Do you wish to take part in a vaccine trial?
    Type 'YES' if yes, type 'NO' if no        """))
    print("Hello", f_name, s_name, "you are", age, "years old, and your eircode is", eircode)
    numlist=["1", "3", "5", "7", "9"]
    if eircode[-1] in numlist:
        print("You must attend Northfield for your vaccine")
    else:
        print("You must attend Eastwood for your vaccine")
    if trial=="NO":
        if age<=12:
            print(f_name, "you will not be recieving a vaccine at this date.")
        elif age>=50:
            print(f_name, "you will recieve the ADENA vaccine.")
        else:
            print(f_name, "you will recieve the MRNA vaccine.")
    if trial=="YES":
        print(random.choice(choices))
    test=str(input("If you have finished entering person's details, type 'END', otherwise press return     "))

medianlist=[4, 5, 9, 8, 10, 17, 99, 77]
medianlist.sort()
if len(medianlist)%2==0:
    print("Median =", medianlist[int(len(medianlist)/2)])
else:
    print("Median =", (medianlist[int((len(medianlist)/2)+0.5)] + medianlist[int((len(medianlist)/2)-0.5)])/2)


