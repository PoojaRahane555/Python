# # \w [a-z A-Z 0-9]
# # \W [not [a-z A-Z 0-9]]
# # \d - [0-9]
# # \D - not[0-9]
# # \b - blank space
# # \A - match only start of string 
# # \Z - match only at end of string

# Program 1:
import re
str = "The meeting will be conducted on 5th, 21st, and 22nd"
fulldig = re.findall(r'\d[\w]*',str)
print(fulldig)
dig = re.findall(r'\b\d[\d]*',str)
print(dig)

# Program 2:
str2 = "an apple a day keeps a doctor away"
charAl = re.findall(r'a[\w]*',str2)
print(charAl)

charA = re.findall(r'\ba[\w]*',str2)
print(charA)

# Program 3:
str3 = "one two three four five 6 seven eight 9 10 eleven"
char5 = re.findall(r'\b\w{5}\b',str3)
print(char5)

char55 = re.search(r'\b\w{5}\b',str3)
print(char55.group())

char5m = re.match(r'\b\w{5}\b',str3)
# print(char5m.group())

# Program 4:
char4Al = re.findall(r'\w{4,}',str3)
print(char4Al)

char4 = re.findall(r'\b\w{3,5}\b',str3)
print(char4)

# Program 5:
onlydig = re.findall(r'\d{1,}',str3)
print(onlydig)

# Program 6:
str4 = 'one two three four five 6 seven eight 9, 10 eleven aa twelve'
ending = re.findall(r't[\w]*\Z',str4)
print(ending)

# Program 7:
str4 = 'one two three four five 6 seven eight 9, 10 eleven aa twelve'
starting = re.findall(r'\A[\w]*',str4)
print(starting)

# Program 8:
str5 = 'one two three four five 6 seven eight 9, 10 aa abc555xyz'
forDig = re.findall(r'\b\d[\w]*\b',str5)
print(forDig)

# Program 9:
str6 = "Pooja-Rahane-7030819999"
# num = re.search(r'\d[\w]*',str6)
num = re.search(r'\d+',str6)
print(num.group())




