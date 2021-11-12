import time
print("""Python
programming
is
great
fun! :)
""")

time.sleep(1)
string=str(input("Give me a nice keyboard smash: "))
finalnum=0
for i in (string):
    if i.isdigit():
        finalnum+=int(i)
print(finalnum)

sentence=str(input("Write a sentence or i take yor liver: "))
print(sentence.replace(" ","-"))

vowelsentence=str(input("Write NOW :"))
