def display(*data): # Tuple arg
    print(type(data))
    print(f'Data contains {data}')

def display_each(*data): # Tuple arg
    for each in data:
        print(type(each))
        print(f'Data contains {each}')

display()
display(1)
display("a",1)
display_each("a",1,True)


