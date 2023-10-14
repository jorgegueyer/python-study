import re

text = "This is python and we are having python2 nad python3 version" 

my_pat = r"\bpython[23]?\b"
print(re.finditer(my_pat, text))

for each in re.finditer(my_pat, text):
    print(f'The match is: {each.group()} starting index: {each.start()}, ending index: {each.end()}')