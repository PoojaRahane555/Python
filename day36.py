# Regular expression:
# \w [a-z,A-Z,0-9]

# Program 1: It gives first occurance for given
import re
str = "color kid yellow kity cup"
result = re.search(r'k\w\w',str)
# print(result.group())
if result:
    print(result.group())

# Program 2: It gives all the occurance for given
str2 = "kidzonia is international preschool for kids"
result2 = re.findall(r'k\w\w',str2)
print(result2)

# Program 3: It gives only first match
str3 = "hello I am learning very interestingig programming language python"
result3 = re.match(r'h\w\w',str3)
print(result3.group())

# Program 4: \W+ non alpha
str4 = "wow! today ,  i have seen : very nice car.  "
result4 = re.split(r'\W+',str4)
print(result4)

# Program 5: Replace
str5 = "I like banana and apple."
result5 = re.sub(r'apple','mango',str5)
print(result5)
