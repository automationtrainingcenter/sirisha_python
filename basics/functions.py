"""
function is a block of code
to declare functions in python we have to use def keyword

def function_name(arg1, arg2 .... argn):
    function definition

pass keyword is used to define empty functions
def function_name():
    pass

functions can take any number of arguments and can return any datatype
function return type dynamic
and function might or might not take argumnets

To overload the funcitons we have to use optional arguments
positional arguments doesn't contain any default values
optional arguments contain default values
"""

k = 10

def sum(a, b):
    print(a+b)

def mul(a, b):
    return a*b

def display(value=30*'*'):
    print(value)


def method2(arg1, arg2 = 10):
    print(arg1+arg2)

def method3(arg1, arg2 ):
    print(arg1*arg2)
# def display():
#     print(30*'*')


def scope():
    # use global keyword to use a global variable instead of local
    global k
    k = 2000
    print(f'inside scope function k = {k}')

sum(10, 20)
display(2098)
# product = mul(10, 10)
# print(product)
print(mul(10,20))

print(f'before calling scope() k = {k}')
scope()
print(f'after calling scope() k = {k}')


method2(100)

method3(arg1= 10, arg2 = 'sirisha')

method3(arg2= 10, arg1 = 'sirisha')
