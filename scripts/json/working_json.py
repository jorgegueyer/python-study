import json

req_file = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\json\\example.json"

fo = open(req_file, 'r')

json_data = json.load(fo) # Dictionary format
print(json_data)
print(json_data.get('glossary'))
print(json_data.get('glossary').get('title'))

fo.close()

my_dict = {'Name':'Jorge', 'skills': ['Java', 'Python', 'bash' 'yaml']}
req_file = "C:\\Users\\jorge\\OneDrive\\workspaces\\Python\\scripts\\json\\my_json.json"

fo = open(req_file, 'w')

json.dump(my_dict, fo, indent=4)

fo.close()
