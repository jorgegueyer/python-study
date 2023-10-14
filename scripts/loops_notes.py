#  Simple for construction, iterating a List
my_list = [0, 1, 2, 3, "hi", 3.2]
for list_value in my_list:
    print(list_value)

# Iterating a Tuple
my_tuple = (0, 1, 2, 3, "hi", 3.2)
for tuple_value in my_tuple:
    print(tuple_value)

# Iterating a String
for each_char in "Hello World":
    print(each_char)

# For loop with if condition inside
numbers = [1,2,5, 9,15,27,36,48,57,63,78,82,92,103]
for number in numbers:
    rem = number % 2
    if rem == 0:
        print(f'{rem} is even')
    else:
        print(f'{rem} is odd')

for each in range(10):
    print("for loop")

i = 0
while i < 10:
    print(f'value: {i}')
    i = i + 1
