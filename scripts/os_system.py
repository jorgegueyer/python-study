import os

# On linux system
os.system("pwd") # -> 0, success code
os.system("ls") # -> 0, success code
os.system("clear") # -> 0, success code

# Unknown command
os.system("sdfasd") # -> different from 0, error

result = os.system("ls")
print(result) # -> code

cmd = "datee"
result = os.system(cmd)
if result == 0:
    print("Command was executed successfully.")
else:
    print("Command failed.")

