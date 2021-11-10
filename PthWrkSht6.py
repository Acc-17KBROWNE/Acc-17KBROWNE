import time
string="Hello There Bob"
string_length=len(string)
print(string_length)
print(string[0])
print(string[4])
print(string[-1])
time.sleep(2)
for ch in string:
    print(ch)
time.sleep(2)
for ch in range(0,len(string)):
    print(string[ch])
time.sleep(2)
for ch in range(0,len(string)):
    print(ch)

time.sleep(1)

string0=" Can I get a bread with no gluten? "
print(string0)
time.sleep(1)
print(string0.upper())
time.sleep(1)
print(string0.lower())
time.sleep(1)
print(string0.count("a"))
time.sleep(1)
print(string0.find("a"))
time.sleep(1)
replaced = string0.replace("a", "o")
print(replaced)
time.sleep(1)
print(string0.islower())
time.sleep(1)
print(string0.isupper())
time.sleep(1)
print(string0.isalnum())
time.sleep(1)
print(string0.isalpha())
time.sleep(1)
print(string0.isdigit())
time.sleep(1)
result=string0.index("no")
print(result)
time.sleep(1)
print(string0.strip(" "))

time.sleep(1)
pal=str(input("Give me a word: "))
pal=pal.upper()
if(pal==pal[::-1]):
    print("The word is a palindrome")
else:
    print("Not a palindrome")
