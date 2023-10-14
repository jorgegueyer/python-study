def sum(a,b):
    print(f'The sum of {a} and {b} is {a+b}')
    return None

def sub(a,b):
    print(f'The sub of {a} and {b} is {a-b}')
    return None

def mult(a,b):
    print(f'The multiplication of {a} and {b} is {a*b}')
    return None

print(f'__name__ is {__name__}')
if __name__ == "__main__":    
    print('This script is executed from this script')
else:
    print('This script is executed by the import in script2.py')