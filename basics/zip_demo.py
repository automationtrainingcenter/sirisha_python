list1 = ['surya', 'teja', 'sirisha', 'john']
list2 = [100, 150, 120, 180]
list3 = [31, 28, 28]

print(type(zip(list1, list2)))

zipped_data = list(zip(list1, list2))
print(zipped_data)

new_zipped_data = list(zip(list1, list2, list3))
print(new_zipped_data)
