import re

text = "This is about python and python is very easy and we are having Python2 vers and Python3 vers"

my_pat = "python[23]?"
# re.split
print(re.split(my_pat,text))
print(re.split(my_pat,text,flags=re.I))
print(re.split(my_pat,text,maxsplit=0,flags=re.I))
print(re.split(my_pat,text,maxsplit=1,flags=re.I))
print(re.split(my_pat,text,maxsplit=2,flags=re.I))

# re.sub
print(re.sub(my_pat,'jython',text))
print(re.sub(my_pat,'jython',text,flags=re.I))
print(re.sub(my_pat,'jython',text,count=0,flags=re.I))
print(re.sub(my_pat,'jython',text,count=1,flags=re.I))

# returning a couple
print(re.subn(my_pat,'jython',text,count=1,flags=re.I))