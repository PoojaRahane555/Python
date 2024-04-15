# program 1:
import os
import sys


f1 = open('info1.txt','a+')

while str != '@':
    str = input(' Please enter your name: ')
    if str != '@':
        f1.write(str + '\n')
f1.seek(0,0)
str2 = f1.read()
print(str2)
f1.close()

# program 2:
fileName = input('Enter the file name: ')

if os.path.isfile(fileName):
    f2 = open(fileName,'r')
else:
    print('file does not exist')
    sys.exit()


countChar = 0
countWord = 0
countLine = 0

for line in f2:
    countLine = countLine + 1
    list = line.split()     #["Pooja","Aarvi","Tanvi","Avnish"]

    countWord = countWord + len(list)
    countChar = countChar + len(line)
print(countChar)
print(countWord)
print(countLine)

f1.close()