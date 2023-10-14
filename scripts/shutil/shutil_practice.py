import shutil


src = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/someFile.txt'

# copyfile
dest = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copyFile.txt'
shutil.copyfile(src, dest)

# copy - keep permissions of the source file
dest = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copy.txt'
shutil.copy(src, dest)

# copy2 - same permissions and same metadata (date, timestamp, permissions, and so on)
dest = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copy2.txt'
shutil.copy2(src, dest)

# copymode - copying permissions only
src_per = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copy2.txt'
dest_per = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copy2.txt'
shutil.copy2(src, dest)

# copystat - copy metadata (timestamp, permissions, and so on), not content
dest = '/mnt/c/Users/jorge/OneDrive/workspaces/Python/scripts/shutil/copy2.txt'
shutil.copystat(src, dest)

# Clone file

# f1 = open('xyz.txt','r')
# f2 = open('pqr.txt','w')
# shutil.copyfileobj(f1,f2)

# copy tree - all the content of the folder and subfolders
# src = '/home/.ssh'
# shutil.copytree(src, '/tmp/ssh')

# remove the tree folder

# shutil.rmtree('/tmp/ssh')

