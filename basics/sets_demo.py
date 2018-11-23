"""
set does not allow duplicates
"""
my_set = {100, 12.4445, 'sirisha', 'python', 123, True, 123}
print(len(my_set))

print(my_set)

my_set.add('django')

print(my_set)

print(my_set.pop())
print(my_set)
my_set.remove(123)
print(my_set)

set_two = {12, 'sirisha', 100, 99}

# set intersection
# my_set.update(set_two)
print(f'intesection of {my_set} and {set_two} is {my_set.intersection(set_two)}')

# set_two.intersection_update(my_set)
# print(set_two)


# set union
print(my_set.union(set_two))
print(my_set)

print(my_set.difference(set_two))

print(my_set.isdisjoint(set_two))
