# every instance method in python class takes self as default argumnet
# self is not a keyword it can be replaced by any word
# self is like this keyword in C# or Java
# self reporesents current class instance
class Student:

    # def __init__(self):
    #     self.name = ''

    def say_hello(self, name):
        self.name = name
        print(f'hello {self.name}')

    def display_my_name(self):
        print(self.name)


# creating an object of the class
s1 = Student()
print(s1)
s1.say_hello('sirisha')
s1.display_my_name()
