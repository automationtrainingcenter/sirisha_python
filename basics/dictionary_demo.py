"""
dictionaries will store the data in key and value pairs
"""

my_dict = {1:'surya', 2:'sirisha', 275:'python'}

dict_two = {4 : 'java', 5 : 'django'}

print(len(my_dict))

# dictionary_ref[key] = value

my_dict[7] = 879.99

print(my_dict[2])

print(my_dict)

print(my_dict.get('python'))

my_dict.update(dict_two)
print(my_dict)

print(type(my_dict.items()))
for item in list(my_dict.items()):
    print(item)

for (k,v) in list(my_dict.items()):
    print(f'{k} = {v}')

print(my_dict.pop(1))
print(my_dict)

print(my_dict.popitem())
print(my_dict)


print(sorted(my_dict.items()))
print(my_dict)
