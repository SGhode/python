class Employee:
    company = "Dell" # This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Created an instance attributes of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the emloyee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")


e1 = Employee(3400, "Shivraj", 3, "Tesla")
print(e1.company) # will always print instance attributes whenever present.
print(Employee.company) # This will always print the class attributes


# Object introspection
print(dir(e1))






