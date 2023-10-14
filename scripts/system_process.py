import subprocess

cmd = 'ls -lrt'

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
# sp = subprocess.Popen(['ls', '-lrt'], shell=False, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

rc = sp.wait()
out,err= sp.communicate()

print(f'The return code is: {rc}')
print(f'OUTPUT is: \n{out.splitlines()}')
print(f'ERROR is: \n{err.splitlines()}')