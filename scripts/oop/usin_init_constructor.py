class Emp(object):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        return None
    
    def display(self):
        print(f'The name is: {self.name}\The salary is: {self.salary}')

emp1 = Emp('John', 25000)
emp1.display()

emp2 = Emp('Sarah', 35000)
emp2.display()