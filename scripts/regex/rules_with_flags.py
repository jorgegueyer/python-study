import re

text = "this is a string ThIs is a new staring THIS"

my_pat = r"this"
print(re.findall(my_pat, text))
print(re.findall(my_pat, text, re.IGNORECASE))
print(re.findall(my_pat, text, re.I)) # re.IGNORECASE

text = """this is a string EnD
this is a secondo line
asfasd this"""

my_pat = r"this"
print(text)
print(re.findall(my_pat, text))

my_pat = r"^this" # Start of the string
print(text)
print(re.findall(my_pat, text))
print(re.findall(my_pat, text, re.MULTILINE))
print(re.findall(my_pat, text, re.M)) # re.MULTILINE
print(re.findall(my_pat, text, re.M|re.I)) # re.MULTILINE and re.IGNOSECASE

my_pat = r"end$" # end of the string
print(re.findall(my_pat, text))
print(re.findall(my_pat, text, re.MULTILINE))
print(re.findall(my_pat, text, re.M)) # re.MULTILINE
print(re.findall(my_pat, text, re.M|re.I)) # re.MULTILINE and re.IGNOSECASE