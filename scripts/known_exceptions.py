# NameError
#print(a)

#TypeError
#print(4+"string")

#FileNotFoundError
#fo = open("unknown.txt")

#ZeroDivisionError
#print(5/0)

try:
    print(a)
except NameError as nameError:
    print(nameError)

try:
    print(4+"string")
except TypeError as typeError:
    print(typeError)

try:
    fo = open("unknown.txt")
except FileNotFoundError as fileNotFound:
    print(fileNotFound)
except Exception as e:
    print(e)


try:
    print(5/0)
except ZeroDivisionError as zeroDivision:
    print(zeroDivision)
except Exception as e:
    print(e)

try:
    print(a)
except Exception as e:
    print(e)
finally:
    print("Executing finally block")