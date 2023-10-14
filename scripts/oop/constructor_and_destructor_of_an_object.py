class Person(object):
    
    def __init__(self,name,age):
        print('An object has been created')
        self.name = name
        self.age = age
        return None
    
    def __del__(self):
        print('Object has been deleted')
        return None
    
   
person = Person('Jorge', 32)

del person