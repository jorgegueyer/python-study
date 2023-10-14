print("Working with Exceptions")

try:
    import fabric
except Exception as e:
    print(e)
    

try:
    print(4/0)
except:
    print("Zero division error")

try:
    fo = open("none.txt")
    print(fo.read())
    fo.close()
except Exception as e:    
    print("Some problem while reading the none.txt:", e)

my_list = [0,1,2]
try:
    print(my_list[3])
except Exception as e:
    print(e)