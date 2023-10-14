import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.43',username='ubuntu',password='Egroj123',port=22)

sftp_client = ssh.open_sftp()

# Getting a file from a remote server
# sftp_client.get('/home/ubuntu/paramiko_download.txt', 'paramiko_download.txt')

# Windows path
#sftp_client.chdir('/home/ubuntu')
#print(sftp_client.getcwd())
#sftp_client.get('demo.txt', 'C:\\Users\\jorge\\Downloads\\demo.txt')

# Uploading a file from the local host
sftp_client.put('transference.txt', '/home/ubuntu/transfer_file_ubuntu_22.04.txt')

sftp_client.close()
ssh.close()