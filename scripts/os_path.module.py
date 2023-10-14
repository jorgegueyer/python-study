import os

print(os.path)
print(os.path.sep)

path = "C:\\Users\\jorge\\test.py"
print(os.path.basename(path)) # -> test.py
print(os.path.dirname(path)) # -> C:\Users\jorge

path1 = "C:\\Users"
path2 = "jorge"
print(os.path.join(path1, path2)) # -> C:\Users\jorge

path = "C:\\Users\\jorge\\test.py"
print(os.path.split(path)) #-> ('C:\Users\jorge'.'test.py')

print(os.path.getsize(path)) # in bytes

path = "C:\\Users\\jorge\\test.py"
print(os.path.exists(path)) # -> True

unkownPath = "C:\\Users\\jorge\\unKown.py"
print(os.path.exists(path)) # -> False

path = "C:\\Users\\jorge\\test.py"
os.path.isfile(path) # -> true

os.path.isdir(path) # ->  False

# ln -s test.py linktest
os.path.islink("linktest") # -> True
os.path.islink("test.py") # -> False
