class Parent1:
    def __init__(self):
        print('parent 1 object created')

class Parent2:
    def __init__(self):
        print('parent 2 object created')

class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print('child object created')


cObj = Child()
