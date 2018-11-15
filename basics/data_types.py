"""
variable is name of a memory location
data type is  classification of data
In Python we have
int
boolean
float
string

type() is used to get the type of the variable
"""

i = 1000
print(f'i = {i}')
print(f'value of i = {i} and type of i = {type(i)}') # int
fi = float(i)
print(type(fi)) # flaot
print(f'value of i after converting to bool is = {bool(i)} and type is = {type(bool(i))}') # bool #True
print(type(str(i))) # str string 1000

f = 10.103
print(f'f = {f}')
print(type(f))
ifl = int(f)
print(f'ifl = {ifl}')
print(type(ifl))
print(type(bool(f)))
print(type(str(f)))



b = False
print(f'b = {b}')
print(type(b))
print(int(b))
print(float(b))
print(str(b))

# string  to boolean conversion
name = 'sirisha'
print(f'name = {name}')
print(type(name))
print(bool(name)) # True

# string to integer conversion
char = '12'
print(f'char = {char}')
print(type(char))
print(int(char)) # integer 1

# string to float conversion
float_string = '12.223'
print(f'float_string = {float_string}')
print(type(float_string))
print(float(float_string)) # flaat 12.223
