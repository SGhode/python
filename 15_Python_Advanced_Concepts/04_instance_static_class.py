class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance Method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Methods
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        


e1 = Employee("Rocky", 45000)
e2 = Employee("Shivraj", 95000)
# print(Employee.company)
# e1.print_info()
# e2.print_info()

# print(e2.sum(55, 45))
# e1.print_company()

e1.change_company("Dell")
print(Employee.company)
