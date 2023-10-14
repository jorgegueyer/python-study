try:
    print(a)
except Exception as e:
    print("Exception occured: ", e)
finally:
    print("This will execute always")


try:
    print(a)
except Exception as e:
    print("Exception occured: ", e)
else:
    print("This will execute if there are no exceptions in try block")
finally:
    print("This will execute always")

try:
    a = 1
    print(a)
except Exception as e:
    print("Exception occured: ", e)
else:
    print("This will execute if there are no exceptions in try block")
finally:
    print("This will execute always")