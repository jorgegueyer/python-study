# raise Exception("Raising an exception")

# raise NameError("Raising an exception")

age = 23
if age > 23:
    print("Valid age")
else:
    raise ValueError("Invalid age")

# assert 4 < 3

age = 20

try:
    assert age > 30
    print("Valid age")
except AssertionError:
    print("Raised with assert because age is less than 30")
except:
    print("Exception happened")