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
vowelsentence=vowelsentence.lower()
length=len(vowelsentence)
ch="a", "e", "i", "o", "u"
count=0
while count != len(vowelsentence):
    ch = vowelsentence[count]
    if ch =="a" or ch=="e" or ch == "i" or ch == "o" or ch == "u":
        print(ch)
    count = count+1
print(length-count)

nohyphen= str(input("Givis a sentence: "))
print(nohyphen.replace("-","""
"""))
