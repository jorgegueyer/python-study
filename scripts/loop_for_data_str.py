my_string = "working with for loop"
print(my_string)

print(" ".join(my_string))
print("\n".join(my_string))

for each_char in my_string:
    print(each_char)

my_list = [1,2,3,4,5]

for each_item in my_list:
    print(each_char)

my_list_tuple = [(0,1),(2,3),(4,5)]
for each_item in my_list_tuple:
    print(each_char)

for x,y in my_list_tuple:
    print(x)
    print(y)

my_list_list = [[0,1],[2,3],[4,5]]
for x,y in my_list_list:
    print(x)
    print(y)

my_dic = {'a':1,'b':2,'c':3}
for key,value in my_dic.items():
    print(f'key: {key} value: {value}')