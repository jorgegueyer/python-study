import os

path = input("Enter your path:")
if os.path.exists(path):
    if os.path.isfile(path):
        print(f'The given path: {path} is a file.')
    else:
        print(f'The given path: {path} is a directory.')
else:
    print(f'The given path: {path} does not exist.on this host.')