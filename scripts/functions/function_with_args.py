def get_add(value1, value2):
    result = value1 + value2
    print(f'The add result is: {result}')
    return None

def get_sub(value1, value2):
    result = value1 - value2
    print(f'The sub result is: {result}')
    return None

def main():
    num1 = eval(input('Enter the first number: '))
    num2 = eval(input('Enter the second number: '))
    get_add(num1, num2)
    get_sub(num1, num2)
    return None

main()