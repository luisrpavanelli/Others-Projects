#   Question 2
#   Create a derived class from the base class
#	Inherits all properties and methods from the base class
#	Initialize the properties differently from the base class
#	Add code to the empty methods
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        return f"{self.salary}"     

class Person:
    def __init__(self,address):
        self.address = address


class Developer(Employee, Person):
    def __init__(self, first_name, last_name, salary, language,address):
        Employee.__init__(self, first_name, last_name, salary)
        Person.__init__(self, address)
        self.language = language
    
    def __str__(self):
        return f"{self.language}"    

dev1 = Developer("Luis","Pavanello", 20000, "Python", "Paraguay")
print(dev1.first_name)
print(dev1.last_name)
print(dev1.salary)
print(dev1.address)
print(dev1.language)

