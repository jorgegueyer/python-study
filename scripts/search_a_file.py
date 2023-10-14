import os
import platform
import string

req_file = input("Enter the name of the file to find:")

if platform.system() == "Windows":
    # Possible disk letters
    pd_name = string.ascii_uppercase
    valid_drivers = []
    for each_driver in pd_name:
        if os.path.exists(each_driver + ":\\"):
            valid_drivers.append(each_driver + ":\\")

    for each_driver in valid_drivers:
        for root, dirs, files in os.walk(each_driver):    
            for file in files:
                if file == req_file:        
                    print(os.path.join(root,file))
else:
    for root, dirs, files in os.walk("/"):    
        for file in files:
            if file == req_file:        
                print(os.path.join(root,file))

                