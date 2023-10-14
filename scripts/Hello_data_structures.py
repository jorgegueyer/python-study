# List
'''
Lists are mutables
'''
x = 5
empty_list = []
my_values = [1,2,3,4.2,"python", "devops", 5.9]
print(bool(empty_list))
print(bool(my_values))
print(my_values,type(my_values))
print(my_values[0])
print(my_values[-1])
print(my_values[5])
print(my_values[-6])
print(my_values[:])
print(my_values[0:])
print(my_values[:3])

my_values[0] = 54
print(my_values[0])

print(f"Count function counts the number of items repeated inside the list: {my_values.count(5)}")

my_values.append("new value")
print(my_values)
my_values.insert(1, 34)
print(my_values)

my_values.extend(["extend value", 98])
print(my_values)

numbers_list = [3,6,4,8,6,9,2,1]

numbers_list.sort()
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)

# Tuple
'''
Tuples are inmutables
'''
empty_tuple = ()
print(bool(empty_tuple))
print(empty_tuple)
my_tuple = (3,4,[5,6,7],8,9)
print(type(my_tuple))
print(bool(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[2][1])
print(my_tuple[2][0])
# my_tuple[0] = 32 does not support item assignment
print(my_tuple[:])
print(my_tuple[0:])
print(my_tuple[3:])
print(my_tuple[:6])
print(my_tuple[3:6])

simple_tuple = 1,
print(simple_tuple,type(simple_tuple))
new_tuple = 2,3,4
print(new_tuple,type(new_tuple))

# Dictionay

empty_dict = {}
print(empty_dict,type(empty_dict))
print(bool(empty_dict))

my_dict = {'fruit':'apple','animal':'fox','number':'one',2:'two'}
print(bool(my_dict))
print(my_dict)
print(my_dict['fruit'])
print(my_dict.get('animal'))
# print(my_dict['three']) throws an exception
print(my_dict.get('three')) # returns none 

my_dict['three'] = 3
print(my_dict)
my_dict['three'] = 33
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

dict_copy = my_dict.copy()
print(id(my_dict), id(dict_copy))

my_new_entry = {'four',4}
my_dict.update(my_new_entry)
print(my_dict)

print(my_dict.pop("four"))
print(my_dict)
removed_entry = my_dict.popitem()
print(my_dict)
print(removed_entry)

new_dict = dict.fromkeys(['one','two','three'])
new_dict['one'] = "uno"
print(new_dict)

my_dict.setdefault('five', 5)
print(my_dict)
print(my_dict.get('five'))

# Set
empty_set = {}
print(bool(empty_set))
my_set = {4,5,6,7,8,9}
print(my_set)
print(bool(my_set))

list_to_set = [1,2,3,4]
new_set = set(list_to_set)

print(new_set.union(my_set))
print(my_set.intersection(new_set))





