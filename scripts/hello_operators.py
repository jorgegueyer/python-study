

print(4 <= 3)
print(4 < 3)
print(4 >= 3)
print(4 > 3)
print(4 == 4)
print(4 != 4)
print(ord('a'))
print(char(97))
print(ord('-'))
print(char(45))

x = 1
y = 2
z = 'Hi'

print(type(x) is type(y))
print(type(x) is not type(y))
print(type(x) is not type(z))

list = [1,2,3,4,5]
print(3 in list)
print(9 in list)

list = ['a','b','c','d']
print('a' in list)
print('z' in list)


print(x < y and 'b' in list)
print(x < y and 'z' in list)
print(not x < y and not 'b' in list)

print(x < y or 'b' in list)
print(x < y or 'z' in list)
print( not x < y or  not 'b' in list)

print(all([2<3,3<4,4<5,5<6]))
print(not all([2<3,3<4,4<5,5<6]))
print(any([2<3,3<4,4<5,5>6]))
print(not any([2<3,3<4,4<5,5<6]))

print(all([2<3,3<4,4<5,5<6]))
print(not all([2<3,3<4,4<5,5<6]))
print(any([2<3,3<4,4<5,5>6]))
print(not any([2<3,3<4,4<5,5<6]))


a = eval(input("Enter the first number:"))
b = eval(input("Enter the second number:"))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
elif a == b:
    print(f"{a} is equal to {b}")

