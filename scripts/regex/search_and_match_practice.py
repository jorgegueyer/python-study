import re

text = "This is for python and there are two major vers python2 and pyton3 in future python4"

my_pat = r"\bpython\b"
print(re.findall(my_pat, text))

my_pat = r"\bpython2\b"
print(re.findall(my_pat, text))

my_pat = r"\bpython\d?\b"
print(re.findall(my_pat, text))

my_pat = r"\bpythonnn[23]?\b"
print(re.findall(my_pat, text))
print(re.search(my_pat, text))

my_pat = r"\bpython[23]?\b"
match_obj = print(re.search(my_pat, text))

if match_obj:
    print("match from ur pattern: ", match_obj.group())
    print("Starting index: ", match_obj.start())
    print("Ending index: ", match_obj.end())
    print("Length: ", match_obj.end() - match_obj.start())
else:
     print("No match found")


text_multiline = """This is for 
python and there are two major 
vers python2 and pyton3 in future python4"""

my_pat = r"\bpython[23]?\b"
match_obj = print(re.search(my_pat, text_multiline))

if match_obj:
    print("match from ur pattern: ", match_obj.group())
    print("Starting index: ", match_obj.start())
    print("Ending index: ", match_obj.end())
    print("Length: ", match_obj.end() - match_obj.start())
else:
    print("No match found")

my_pat = r"\bpython[23]?\b"
match_obj = print(re.match(my_pat, text_multiline))



