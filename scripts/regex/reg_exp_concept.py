import re

my_str = "Python is simple and it is easy"

print(my_str.split("is"))

print(re.split("i[st]", my_str))