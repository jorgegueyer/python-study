import re

text = "This is a python and it is easy -to learn @"

my_pat = "is"
result = re.findall(my_pat, text)
print(result)
print(len(result))

my_pat = "i[st]"
result = re.findall(my_pat, text)
print(result)

my_pat = "[a-d]" #[abcd]
result = re.findall(my_pat, text)
print(result)

my_pat = "\\w" #[a-zA-Z]
result = re.findall(my_pat, text)
print(result)

my_pat = "\\w\\w" #[a-zA-Z]
result = re.findall(my_pat, text)
print(result)

numbers = "This is a python3, and it is easy 4 learning python2. @"

my_pat = "\\d" #[0-9]
result = re.findall(my_pat, numbers)
print(result)

my_pat = "python\\d" #python[0-9]
result = re.findall(my_pat, numbers)
print(result)

my_pat = "." # any character
result = re.findall(my_pat, numbers)
print(result)

my_pat = ".." # any character
result = re.findall(my_pat, numbers)
print(result)

my_pat = "..." # any character
result = re.findall(my_pat, numbers)
print(result)

my_pat = "\." # any character
result = re.findall(my_pat, numbers)
print(result)

text = "This is my ip of the a deb server: 255.100.102.103 345345345234523452345"

my_pat = "\d\d\d.\d\d\d.\d\d\d.\d\d\d" 
result = re.findall(my_pat, text)
print(result)

my_pat = "\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d" 
result = re.findall(my_pat, text)
print(result)