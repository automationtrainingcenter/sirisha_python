"""
to read input from the console we have to use input()
input() always returns string type
"""

# print('enter your name')
# name = input()
name = input('enter your name \n')
print('your name is ', name)

"""
formatted strings
"""
interseted_course = input('which course are you interested? \n')
# .format() is used till 3.6
print('Hi, {} and you are interested in {}'.format(name, interseted_course))

# from 3.6 we have f strings
print(f'Hi, {name} and you are interested in {interseted_course}')
