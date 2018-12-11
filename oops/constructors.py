class Employee:
# class variable
    company = 'ssts';

    def __init__(self, name, address, phNum = ''):
        self.name = name
        self.address = address
        self.phNum = phNum

    def display_emp_details(self):
        print(f'name = {self.name} address = {self.address} phNum = {self.phNum} salary = {self.salary} company = {Employee.company}')

    def change_address(self, new_address):
        self.address = new_address

    def salary(self, salary):
        self.salary =salary

    @classmethod
    def change_company_name(cls, new_company_name):
        cls.company = new_company_name



e1 = Employee('sirisha', 'lingampally', '9876543210')
e1.salary(200000)
e1.display_emp_details()
# we can access class variables and methods using class name
print(Employee.company)
Employee.change_company_name('Sun Shine')
e2 =Employee('surya', 'lingampally')
e2.salary(100000)
e2.display_emp_details()
e2.change_address('kukatpally')
e2.display_emp_details()
