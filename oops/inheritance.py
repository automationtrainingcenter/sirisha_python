"""
single A -> B
multi level A -> B -> C
heirarchical A -> B A -> C
multiple A -> C B -> C
hybrid combination of heirarchical and multiple
"""

class Parent:
    def __init__(self):
        print('parent object created')

    def parent_method(self):
        print('this is parent method')


class Child(Parent):
    def __init__(self):
        super().__init__()
        print('child object created')

    def child_method(self):
        print('this is child method')

class SubChild(Child):
    def __init__(self):
        super().__init__()
        print('sub child object created')

    def sub_child_method(self):
        print('this is sub child method')


class Child2(Parent):
    def __init__(self):
        super().__init__()
        print('child2 object created')


# cObj = Child()
# c2Obj = Child2()

# scObj = SubChild()
# cObj.child_method()
# cObj.parent_method()

# pObj = Parent()
# pObj.parent_method()
