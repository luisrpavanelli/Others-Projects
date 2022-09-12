#Question 1 - Create a base class with:
#	Three properties initialized at construction
#	One empty classmethod


#	One empty instance method
# Python program to demonstrate
# classes

class Person:
	
	# init method or constructor
	def __init__(self, name):
		self.name = name
	
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = Person('Vigoorian')
p.say_hi()


#Instance Method

class Employee:
    company = "youtube"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_email(self):
        return f'{self.first_name}.{self.last_name}@{Employee.company}.com'

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name    

    @staticmethod
    def static_method():
        print("This is a static method")

Employee.change_company("google")


emp1 = Employee('luis', 'pavanello')
print(emp1.get_email())

Employee.static_method()
emp1.static_method()

