import os
import sys

path = input("Enter your directory path:")

if os.path.exists(path):
    dir_files = os.listdir(path)
else:
    print(f'{path} is an invalid path')
    sys.exit()

for file_or_dir in dir_files:
    if os.path.isfile(file_or_dir):
        full_path = os.path.join(path, file_or_dir)
        print(f'{full_path} is a file.')
    else:
        print(f'{file_or_dir} is a directory.')