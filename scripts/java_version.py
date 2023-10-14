import subprocess

command = "java -version"

sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)

rc = sp.wait()

o,e= sp.communicate()

if rc == 0:
    if bool(o) == True:
        print(o)
    if bool(o) == False and bool(e) == True:
        for each_line in e.splitlines():
            if "version" in each_line:
                print(each_line.split()[2])
else:
    print("Command was failed and error is: ", e)