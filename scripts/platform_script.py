import platform as pt

print(dir(pt))
print(len(dir(pt)))
#print(help(pt))

print(pt.system())
print(f"This is {pt.system()} os.")
print(f"This is the Python version: {pt.python_version()}.")
print(pt.python_version_tuple())
print(pt.machine())
print(pt.platform())
print(pt.architecture())
print(pt.processor())
print(pt.node())
