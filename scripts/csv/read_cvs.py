import csv

req_file = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\csv\\info.csv"

fo = open(req_file, 'r')

data = csv.reader(fo,)
for row in data:
    print(row) 

fo.close()

req_file = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\csv\\info_delimiter.csv"
fo = open(req_file, 'r')
data = csv.reader(fo, delimiter="|")

header = next(data) # move the cursor to the first position
print(header)

print("The number rows are: ", len(list(data)))

for row in data:
    print(row) 

fo.close()

