'''
It contains letters, numbers and underscore.
It should not a keyword.
Cannot contain spaces.
It should not start with a number.
Case-sensitive
'''

x = 4
print(x)
print(type(x))
y = 5.6
print(y)
print(type(y))

z = bool(0)
print(z, type(z))

cadena = "Python"
print(cadena[-1])
print(cadena[0])
print(cadena[0:3])
print(cadena[:3])

print(f"The lenght is : {len(cadena)}")

print(cadena.lower())
print(cadena.upper())
print(cadena.startswith("P"))
print(cadena.swapcase())
print(cadena.title())
print(cadena.isupper())
print(cadena.islower())
print(cadena.isspace())
print(cadena.istitle())
print(cadena.isalpha())
print(cadena.isnumeric())

print("*".join(cadena))
print("\t".join(cadena))
print("\n".join(cadena))

print(f"{cadena.center(30)}")
print(f"{cadena.zfill(10)}")

print(cadena.strip("p"))
print(cadena.strip("P"))
print(cadena.strip("n"))

cadena = "   python   "
print(cadena.strip())

cadena = "Python is a python"
print(cadena.rstrip("python"))
print(cadena.lstrip("Python"))
print(cadena.split())
print(cadena.split("is"))

print(cadena.count("o"))
print(cadena.count("P"))

print(cadena.index("a"))
print(cadena.index("is"))
# print(cadena.index("house")) --> it throws an exception

print(cadena.find("a"))
print(cadena.find("is"))
print(cadena.find("house")) # It doesn't throw an exception

'''
bool(empty) = False -> bool(0), bool(None), bool([]), bool(()), bool({})
bool(non_empty) = True
'''
z = bool(1)
print(z, type(z))


z = bool(73)
print(z, type(z))

z = str(x)
print(z, type(z))

print("{} {} {}".format(x, y, z))

print(f"{x} {y} {z}")

multiple_lines = '''
There are
multiple 
lines
'''

print(multiple_lines)

del x
del y
del z
del cadena
del multiple_lines