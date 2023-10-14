#sfile = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\file_text\\source.txt"
#dfile = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\file_text\\destination.txt"

sfile = input("Enter the source file: ")
dfile = input("Enter the destination file: ")

# sfo = open(sfile, 'r') # 'r' is the default mode
sfo = open(sfile)
scontent = sfo.read()
sfo.close()

dfo = open(dfile, 'w')
dfo.write(scontent)
dfo.close()