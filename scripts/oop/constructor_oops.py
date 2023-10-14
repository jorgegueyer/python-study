class Emp:

    count = 0

    def __init__(self):        
        print('This is a init method')
        Emp.count = Emp.count + 1
        return None

    def display(self):
        print('This is a display method')
        return None

emp1 = Emp()
emp1.display()

emp2 = Emp()
emp2.display()

print('The number od objects created from Emp class are', Emp.count)