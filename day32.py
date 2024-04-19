# File handling:
# three modes ==>  read, write, append(to add extra in previous file)
# f = open('file name',mode='r',buffering,encoding=None,errors=None,newline=None,closefd=None)
#buffering:
#  buffering default value is 4096-8192 bytes.buffering value can't be zero in text mode only gives in binary mode.
# positive integer value is used to set buffering size for file.
# encoding: linux utf-8(given value)
# encoding type is used to decode and encode file.used in text mode only.default value depends on Os.
# windows: cp125(default encoding value)
# errors:
# represents how encoding and decoding errors are to be handled.
# can not used in binary mode.standard values are strict,ignore,replace etc.,
# new line:
# it can be \n,\r\,\r\n

# file object variable - name,mode,encoding,closed(return boolean value)
# f.name, f.mode
# file obj.methods:
# readable() -check wether file is readable or not.true(file is readable).false(file is not readable)
# writable() -check wether file is writable or not.true(file is writable).false(file is not writable)
# f.readable() gives true f.writable gives false for mode 'r'. mode 'w+' gives true for both methods.

# isfile():
# check file exist or not.belongs to path module which is sub module of OS module.
# import os
# os.path.isfile(filename)
import os 
if os.path.isfile('file name'):
    open('file name')
    # operation
    f.close()  # type: ignore
else:
    print('file does not exists')

# Write:
f = open('info1.txt','w');               #creation of object
number = input("Enter the number: ")     #taking input from user
f.write(number)                         #writing to the file
f.close()                               #closing the file-mandatory

# Read:
f = None
try:
    fileName = input("Enter the fileName: ")
    f = open('info1.txt','r')
    number = f.read()
    print(number)
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()

print("Bye EveryOne....")

# Program 1:
f1 = open("info2.txt",'w')
str = input("Enter your Name: ")
f1.write(str)
f1.close()

# program 2:
str = input('Enter your file name: ')
f1 = open('info2.txt','r')
str = f1.read()
f1.close()

# Program 3:

f1 = None
try:
    str = input("Please enter your file name: ")
    f1 = open("info2.txt",'r')
    str = f1.read()
    print(str)
except FileNotFoundError:
    print("file not found")
finally:
    if f1 is not None:
        f1.close()

# program 4:
f2 = open('info3.txt','w')
while str != '@':
    str = input("Enter Name: ")
    if str != '@':
        f2.write(str + '\n')
f2.close()
    

