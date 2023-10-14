import re

text = "it is apython and it is easy to learn python    apythonb"

my_pat = "i[it]"
print(re.findall(my_pat, text))

my_pat = "python$" # $ last occurency (at the end)
print(re.findall(my_pat, text))

my_pat = "\\bpython" # python with a previous white space
print(re.findall(my_pat, text))

my_pat = r"\bpython" # python with a previous white space
print(re.findall(my_pat, text))

my_pat = r"python\b" # python with a white space at the end
print(re.findall(my_pat, text))

my_pat = r"\bpython\b" # python with white spaces at the both places
print(re.findall(my_pat, text))

my_pat = r"\Bpython\B" # None white spaces at the both places
print(re.findall(my_pat, text))

my_pat = "\\t" # Tab
print(re.findall(my_pat, text))