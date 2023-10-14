class Tomcat(object):

    def __init__(self, home, ver):
        self.home = home
        self.ver = ver

    def display(self):
        print("This is from Tomcat class")
        print(self.home)
        print(self.ver)


# Inheritance
class Apache(Tomcat):
    def __init__(self, home, ver):
        self.home = home
        self.version = ver

    def display(self):
        print("This is from Apache class")
        print(self.home)
        print(self.version)

tom_ob = Tomcat('/home/tomcat9', '7.9')
apa_ob = Apache('/home/httpd', '2.4')

tom_ob.display()
apa_ob.display()