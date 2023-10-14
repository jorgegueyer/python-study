#!/bin/python
import os

def get_all_tomcats():
    list_of_config_files = []
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file == 'server.xml':
                list_of_config_files.append(os.path.join(r, each_file))
    return list_of_config_files

def display_details(home_conf_files):
    for key in home_conf_files.keys():
        print(f'Info for {key}')
        print(f'The Tomcat home is:', home_conf_files[key][0])
        print(f'The Tomcat config file is:', home_conf_files[key][1])
    return None


def main():
    print('Finding list of tomcats...')
    list_of_tomcats = get_all_tomcats()
    cnt = 1
    home_conf_files = {}
    for each_config_file in list_of_tomcats:
        t_home = os.path.dirname(os.path.dirname(each_config_file))
        t_cnf_file = each_config_file
        home_conf_files['tomcat' + str(cnt)] = [t_home, t_cnf_file]
        cnt += 1
    display_details(home_conf_files)
    return None

if __name__ == "_main__":
    main()