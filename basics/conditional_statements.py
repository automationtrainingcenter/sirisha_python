"""
conditional statements which are used to validate expressions
simple if
else if -- elif
else if ladder
nested if

In python we don't have {} for blocks
block starts with :
statements of that block must intended with either space or tab

in keyword is used to verify an value is present in a collection of values
"""
# print('surya' in 'surya prakash')

# num = input('enter a number')
# num = int(num)

# num = int(input('enter a number '))

# simple if
# if num > 0:
#     print(f'{num} is positive')
#
# # if else
# if num % 2 != 0:
#     print(f'{num} is odd)
# else:
#     print(f'{num} is even')


# else if
first_number = int(input('enter first number '))
second_number = int(input('enter second number '))
#
# if first_number > second_number:
#     print(f'first_number {first_number} is bigger')
# elif second_number > first_number:
#     print(f"second_number {second_number} is bigger")
# else:
#     print(f'first_number {first_number} = second_number {second_number}')


# nested if
if first_number != second_number:
    if first_number > second_number:
        print(f'first_number {first_number} is bigger')
    else:
        print(f"second_number {second_number} is bigger")
else:
    print(f'first_number {first_number} = second_number {second_number}')
