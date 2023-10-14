class Emp:

    count = 0

    def assign_name_age_salary(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.increase_count_for_emp()
        return None

    def display_datils(self):
        print(f'The name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
        return None
    
    def increase_count_for_emp(self):
        Emp.count = Emp.count + 1
    
emp1 = Emp()
emp1.assign_name_age_salary('John', 34, 4500)
emp1.display_datils()

emp2 = Emp()
emp2.assign_name_age_salary('Sarah', 29, 5500)
emp2.display_datils()

print(Emp.count)