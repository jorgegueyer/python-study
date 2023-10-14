class Person(object):

    def assign_name_and_age(self,name,age):
        self.name = name
        self.__age = age
        return None
    
    def display(self):
        print(self.name, self.__age)
        self.__operation()
        return None
    
    def __operation(self):
        print('This a private method')
    
person = Person()
person.assign_name_and_age('John', 34)

person.display()
print(person.name)
# print(person.__age) private attribute
# person.__operation() private method