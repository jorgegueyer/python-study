cnt = 1
while cnt <= 5:
    print("Hello")
    cnt = cnt + 1

# Control statements

# break
# continue
# pass

for each in [1,2,5,8,12,16,17]:
    if each != 13:
        break
    print(each)

for each in range(1,11):
    if each != 7:
        print(each)

for each in range(1,11):
    if each == 7:
        continue
    print(each)