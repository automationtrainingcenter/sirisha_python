"""
polymorphysm means one object behaves differently based on environment or input
two types
run time polymorphysm : method overloading: is possible in python by optional arguments
compile time polymorphysm : method overriding : is possible by inheritance

how to call parent class method using child class objects
how to call child class method using parent class objects

"""
class Parent:
    def methodOne(self):
        print('parnet class method one')

    def methodTwo(self):
        print('parent class method two')


class Child(Parent):
    def methodOne(self):
        super().methodOne()
        print('child class method one')

c =Child()
print(type(c))
# super(Child).methodOne()
c.methodOne() #child class method
c.methodTwo() # paretn class method
