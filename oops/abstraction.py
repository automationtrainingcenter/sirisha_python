"""
hiding the implementaion details of methods
python have abstract classes only
"""
from abc import ABC, abstractmethod

class Employee(ABC):
    def setEmployeeDetails(self):
        print('employee details added')

    @abstractmethod
    def getEmpName(self):
        pass

class Employer(Employee):
    def getEmpName(self):
        print("returning emp name")

e = Employer()
e.setEmployeeDetails()
e.getEmpName()
