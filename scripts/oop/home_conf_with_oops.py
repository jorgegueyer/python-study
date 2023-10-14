#!/bin/python
import os

class Tomcat(object):
    def get_conf_file(self, server_xml):
        self.t_home = os.path.dirname(os.path.dirname(server_xml))
        self.conf_file = server_xml
        return None
    
    def display_details(self):
        print(f'The Tomcat home is:', self.t_home)
        print(f'The Tomcat config file is:', self.conf_file)
        return None

def get_all_tomcats():
    list_of_config_files = []
    for r,d,f in os.walk("/"):
        for each_file in f:
            if each_file == 'server.xml':
                list_of_config_files.append(os.path.join(r, each_file))
    return list_of_config_files


def main():
    print('Finding list of tomcats...')
    list_of_tomcats = get_all_tomcats()
    tomcat_objects = []
    for each_file in list_of_tomcats:
        tomcat_object = Tomcat()
        tomcat_object.get_conf_file(each_file)
        tomcat_objects.append(tomcat_object)

    for each_tomcat in tomcat_objects:
        each_tomcat.display_details()

    return None

if __name__ == "_main__":
    main()