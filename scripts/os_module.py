import os

print(help(os))
print(dir(os))

print(os.sep)

# As pwd command
print(os.getcwd())

# As cd command, in order to change the current dir
os.chdir("C:\\Users\\jorge")

# As ls command, in order to list the folder and files contained in the current dir
os.listdir()
# Specifying a dir
os.listdir("C:\\Users\\jorge")

# As mkdir command, in order to create a new folder
os.mkdir("newFolder")

# In order to create sub-content recursively
os.makedirs("newFolder/SubPath/subFolder")

# For removing a file
os.remove("oldFile")

# For removing a folder recursively
os.removedirs("oldFolder/SubPath/subFolder")

# For removing a folder
os.rmdir("oldFolder")

# As a mv command, in order to rename a folder or a file
os.rename("oldName", "newName")

# As env command
print(os.environ)

# In order to get the pid of the process
os.getpid()