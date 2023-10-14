#!/usr/local/bin/python3

import os

req_path = input("Enter your directory:")

if not os.path.exists(req_path):
    print(f'The given path {req_path} does not exist.')
    exit()
elif os.path.isfile(req_path):
    print(f'The given path {req_path} is a file. Please pass only a directory')
    exit()

all_files_dirs = os.listdir(req_path)

if len(all_files_dirs) == 0:
    print(f'The given path {req_path} is empty.')
else:
    req_ext = input("Enter the required extension:")    
    for each_file_dir in all_files_dirs:
        if each_file_dir.endswith(req_ext):
            print(os.path.join(req_path, each_file_dir))
    