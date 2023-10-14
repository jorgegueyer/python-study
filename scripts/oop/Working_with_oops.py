#!/bin/python
import os


def  get_details_for_each_tomcat(server_xml):
    tcf = server_xml
    th = os.path.dirname(os.path.dirname(server_xml))    
    return tcf,th

def display_details(tomcat_file,tomcat_path):
    print(f'The tomcat config file is: {tomcat_file}\nThe tomcat home is: {tomcat_path}')
    return None

def main():
    tomcat7 = "/home/Automation/tomcat7/conf/server.xml"
    tomcat9 = "/home/Automation/tomcat9/conf/server.xml"

    tomcat_file,tomcat_path = get_details_for_each_tomcat(tomcat7)
    display_details(tomcat_file, tomcat_path)
    tomcat_file,tomcat_path = get_details_for_each_tomcat(tomcat9)
    display_details(tomcat_file, tomcat_path)

    return None

if __name__ == "_main__":
    main()