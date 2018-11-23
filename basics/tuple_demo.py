"""
tuples are immutable list
"""

my_tuple = (24,23.33, 'sirisha', 10, 24, False)
print(my_tuple)

print(my_tuple[0])
# my_tuple[0] = 12 # tuple does not support item assignment

tuple_two = (24, 55, 66)
print(my_tuple+tuple_two)
print(len(my_tuple))


print(my_tuple[::])

print(my_tuple[::-1])

print(my_tuple.count(24))

print(my_tuple.index(10))

const_tuple = (14,)
print(type(const_tuple))

index = my_tuple.index('sirisha')

print(my_tuple[:index]+('python',)+my_tuple[index:])

for item in my_tuple:
    print(item)
