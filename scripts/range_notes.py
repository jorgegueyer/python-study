print(range(5)) # -> range(0,5)
print(range(3)) # -> range(0,3)

print(list(range(5))) # -> [0,1,2,3,4,5]
print(list(range(3))) # -> [0,1,2,3]

print(list(range(1,3))) 

print(list(range(1,3,1)))

print(list(range(0,20,2)))
print(list(range(1,20,2)))
print(list(range(0,21,2)))
print(list(range(10,2))) # -> []
print(list(range(10,2,-1))) # -> [10, 9, 8, 7, 6, 5, 4, 3]

print(list(range(-2,-10))) # -> []
print(list(range(-2,-10,-2))) # -> [-2, -4, -6, -8]


print(list(range(0,101,2)))
print(list(range(1,101,2)))

my_list = [0,1,4,"hi"]

print(list(range(len(my_list))))

for each_index in range(len(my_list)):
    print(f'[{each_index}] -> {my_list[each_index]}')