#!/usr/local/bin/python3
import os

def main():
    req_path=input('Enter the path to change working dir: ')
    print("The current working directory is: ", os.getcwd())

    try:
        os.chdir(req_path)
        print("Now the new working dir is: ", os.getcwd())
    except FileNotFoundError:
        print("The given path is not a valid path")
    except NotADirectoryError:
        print("The given path is a file path. So cannot change the working directory")
    except PermissionError:
        print("Don't have access for the given path. So cannot change the working directory")

if __name__ == "__main__":
    main()