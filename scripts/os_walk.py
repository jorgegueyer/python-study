# find path -name *.txt
# /home/xyz
# /home/xyz/dir1
# /home/xyz/dir1/sub1
# sudo find / -iname host.conf
# sudo su -

import os

path = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts"

print(list(os.walk(path))) # -> [('C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts',[all the folders],[all the files]), and continue adding the tuples of the subfolders, ...]
print("----------")
for each in os.walk(path):
    print(each)
    
for root, dirs, files in os.walk(path):
    if len(files) != 0:
        print(root)
        for file in files:        
            print(os.path.join(root,file))