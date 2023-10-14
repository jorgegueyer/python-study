def my_function_1():
    x = 5 # Local variable
    global y # For the downstream
    y = 20 # Local variable
    print("Welcome to functions")
    print("x value from fun1: ", x)
    print("y value from fun1: ", y)
    my_function_2(40)
    return None

def my_function_2(z):
    print("Thanks you")
    print("x value from fun2: ", x)
    print("y value from fun2: ", y) # out of scope, but with global, it is visible
    print("z value from fun2: ", z)
    return None


x = 10 # Global variable
my_function_1()