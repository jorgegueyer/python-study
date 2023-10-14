import re

text = "This is a pythonnnn and python3"

my_pat = r"python"
print(re.findall(my_pat, text))

my_pat = r"pythonn"
print(re.findall(my_pat, text))

my_pat = r"\bpython{4}\b"
print(re.findall(my_pat, text))

text = "This is a pythonnnn and python aaa haaadf xyzaaaaaaaa"

my_pat = r"\ba{3}\b"
print(re.findall(my_pat, text))

my_pat = r"a{8}"
print(re.findall(my_pat, text))

my_pat = r"\bxyza{8}\b"
print(re.findall(my_pat, text))

text = "xz xaz asdfa sdf xaaz xaaaaaaaaz xaaaaz"

my_pat = r"\bxaz\b"
print(re.findall(my_pat, text))

my_pat = r"\bxa{1,4}z\b" # 1, 2, 3 or 4 times
print(re.findall(my_pat, text))

my_pat = r"\bxa{2,}z\b" #  two or more times
print(re.findall(my_pat, text))

my_pat = r"\bxa{1,}z\b" # once or more
print(re.findall(my_pat, text))

my_pat = r"\bxa+z\b" # once or more time
print(re.findall(my_pat, text))

my_pat = r"\bxa*z\b" # zero or more time
print(re.findall(my_pat, text))

my_pat = r"\bxa?z\b" # zero or once
print(re.findall(my_pat, text))