import os
import time
import platform

def mycode(cmd1, cmd2):    
    print("Please wait. Cleaning the screen...")
    os.system(cmd1)
    time.sleep(2)

    print("Please wait. Finding the list of dir and files.")
    os.system(cmd2)
    time.sleep(2)

if platform.system() == "Windows":
    mycode("cls", "dir")
else:
    mycode("clear", "ls -lrt")