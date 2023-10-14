import re

text = "This is about python. Python is very easy to learn and we have two major versions: Python2 and Python3"

my_pat = r"\bPython[23]?\b"

print(re.findall(my_pat, text, flags=re.I))
print(re.search(my_pat, text, flags=re.I))
print(re.split(my_pat, text))

pat_ob = re.compile(my_pat,flags=re.I)
print(pat_ob)

print(pat_ob.findall(text))
print(pat_ob.search(text))