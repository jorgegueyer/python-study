# Working with text files

fo = open('newdemo.txt','w')
print(fo.mode)
print(fo.readable())
print(fo.writable())
fo.close()

fo = open('ramdon.txt', 'w')
fo.write("This is a first line\n")
fo.write("This is the second line\n")
fo.close()

my_content = ['This is the line number: 1', 'This is the line number: 2', 'This is the line number: 3']
fo = open('ramdon.txt', 'w')
fo.writelines(my_content)
fo.close()

my_content = ['This is the iteration number: 1', 'This is the iteration number: 2', 'This is the iteration number: 3']
fo = open('with_loop.txt', 'w') # create a new file each time
for each_line in my_content:
    fo.write(each_line + '\n')
fo.close()

my_content = ['This is the iteration number: 1', 'This is the iteration number: 2', 'This is the iteration number: 3']
fo = open('with_loop.txt', 'a') # append
for each_line in my_content:
    fo.write(each_line + '\n')
fo.close()

fo = open('with_loop.txt', 'r') # read
data = fo.read()
fo.close()
print(data)

fo = open('with_loop.txt', 'r') # read
data = fo.readlines()

for each_line in data:
    print(each_line)

for each in range(3):
    print(data[each])

fo.close()
