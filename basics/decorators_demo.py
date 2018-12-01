"""
this program explains decorators in Python
decorator is nothing but a function. it will take a function as an argument and return one more function
it will modify the input function and returns that modified function
"""

# funciton inside another function
def hello(name = 'sirisha'):
    print(f'hello {name}')

    def greet():
        print('hi how are you')
    def welcome():
        if name == 'sirisha':
            print('welcome')
        else:
            print('hey new user welcome')
    greet()
    welcome()

# hello()

# function return another function
def outer_func():
    print('this is outer functiom')

    def inner_func():
        return '\t this is inner function'

    return inner_func;

# my_func = outer_func()
# print(my_func())

# passing function as an argument to another function
def function2(a, b):
    print('this is function 2',a+b)

def function1(func, a, b):
    print('this is function1')
    func(a, b)
    print('this is end of function 1')

function1(function2, 10,12)


# our own decorator

# def my_decorator(func):
#
#     def dec_func():
#         print('decorating basic')
#         func()
#         print('decorated basic')
#     return dec_func
#
# basic()
# f = my_decorator(basic)
# f()

def my_decorator(func):
    def dec_func():
        print('decorating')
        func()
        print('decorated')
    return dec_func

@my_decorator
def basic():
    print('i am basic')

basic()

@my_decorator
def another_fun():
    print('another fucntion with decoration')
another_fun()
