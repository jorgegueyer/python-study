def sum(value1, value2):
    return value1 + value2

def main():
    a = eval(input("Enter the first number: "))
    b = eval(input("Enter the second number: "))
    result = sum(a, b)
    print(f'The sum of {a} and {b} is: {result}')
    return None

main()

