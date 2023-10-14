import csv

req_file = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\csv\\demo.csv"
fo = open(req_file, 'w', new_line="")
csv_writer = csv.writer(fo, delimiter=',')
csv_writer.writerow(['S_No','Name','Age'])
csv_writer.writerow([1,'John','33'])
csv_writer.writerow([2,'Cliton','55'])
'''
my data = [['S_No','Name','Age'], [1,'John','33'], [2,'Cliton','55']]
csv_writer.writerows(my_data)
'''
fo.close()