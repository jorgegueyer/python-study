class Emp(object):

    def __init__(self):
        print('This is a init method')
        return None

    def name_salary(self, name, salary):
        self.name = name
        self.salary = salary
        return None
    
    def display(self):
        print(f'The name is: {self.name}\The salary is: {self.salary}')

emp1 = Emp()
emp1.name_salary('John', 25000)
emp1.display()

emp2 = Emp()
emp2.name_salary('Sarah', 35000)
emp2.display()
