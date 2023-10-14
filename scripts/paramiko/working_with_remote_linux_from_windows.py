import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.43',username='ubuntu',password='Egroj123',port=22)

stdin, stdout, stderr = ssh.exec_command('whoami')

print("The output is:")
print(stdout.readlines())

print("The error is:")
print(stderr.readlines())

ssh.close()