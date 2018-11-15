# this program explains  operators in python
i1 = int(input("enter first number\n"))
i2 = int(input("enter second number\n"))
print(f'i1 = {i1}\ni2 = {i2}')

"""
arithmatic operators
addition
subtraction
multiplication
division which gives quotient with floating point values
floor division which gives quotient with integer values
modular division gives remainder
power of a given number
"""
print('addition of i1 and i2 is ', i1 + i2)

print('subtraction of i1 and i2 is', i1 - i2)

print('multiplication of i1 and i2 is', i1 * i2)

print('division of i1 and i2', i1 / i2)

print('floor division of i1 and i2 is', i1 // i2)

print('modular division of i1 and i2 is', i1 % i2)

print('power of i1 and i2', i1 ** i2)

"""
Comparasion Operators
equality == compares given two values are equal or not
not equal != compares given two value are equal or not
greater than > compares left operand is greater than right operand
greater than or equal >= compares left operand is greater than or equal to left operand
less than < compares given left operand is less than right operand
less than or equal <= compares given left operand is less than or equal to right operand
"""
print(30 * '*')

print(f'{i1} == {i2} : ', i1 == i2)

print(f'{i1} != {i2} : ', i1 != i2)

print(f'{i1} > {i2} : ', i1 > i2)

print(f'{i1} >= {i2} : ', i1 >= i2)

print(f'{i1} < {i2} : ', i1 < i2)

print(f'{i1} <= {i2} : ', i1 <= i2)

"""
assignment operators
= assigns right operand value to the left operand
+= assigns the sum of left and right operand to left operand
-= assigns the difference of left and right operand to left operand
*= assigns the multiplication of left and right operand to left operand
/= assigns the division of left and right operand to left operand
//= assigns the floor division left and right operand to left operand
%= assigns the modular division left and right operand to left operand
**= assigns the power of left and right operand to left operand
"""
a = 5
b = a
print('b = a', a, b)
b += a  # b = b + a
print('b += a', a, b)
b -= a  # b = b - a
print('b -= a', a, b)
b *= a  # b = b * a
print('b *= a', a, b)

"""
Logical operators
and - it will return true if both the operands are true
or - it will return false if both the operands are false
not - it will complement the given operand

Logical operators can be used with numbers, strings and booleans
any positive number is true and 0 is false
any string value is true and empty string "" is false
"""
print(30 * "*")
i1 = 5  # true
i2 = 2  # false

s1 = "sneha"
s2 = ""

b1 = True
b2 = False

result = i1 and i2
print("i1 and i2 = ", result)  # false

result = i1 or i2
print("i1 or i2 = ", result)  # true

result = not i1
print("not i1 = ", result)  # false

result = s1 and s2
print("s1 and s2 = ", result)

result = s1 or s2
print("s1 or s2 = ", result)

result = not s2
print("not s2 = ", result)

result = b1 and b2
print("b1 and b2 = ", result)

result = b1 or b2
print("b1 or b2 = ", result)

result = not b1
print("not b1 = ", result)

"""
Bitwise operators
& converts given operands to binary and compares each bit and operation
| converts given operands to binary and compares each bit or operation
~ converts given operand to binary and complements each bit
"""
print(30*"*")
print("i1 & i2 = ", i1 & i2)

print("i1 | i2 = ", i1 | i2)

print("~i2 = ", ~i2)
print(bin(i2))
print(bin(~i2))
