import sys

if len(sys.argv) != 3:
    print(f'''
        
        Usage:
        
        {sys.argv[0]} arg1 arg2 = [lower|upper|title]
        
        Example:
        
        python {sys.argv[0]} "Some String" lower
        
    ''')
    sys.exit()

usr_string = sys.argv[1]
usr_action = sys.argv[2]

if usr_action=="lower":
    print(usr_string.lower())
elif usr_action=="upper":
    print(usr_string.upper())
elif usr_action=="title":
    print(usr_string.title())
else:
    print("Invalid option. Please, you must select a valid option from the following list: loer/upper/title")