"""
List is collection of objects
lists are index based
to add the data use the append() method
to retrive and update the data we can use index values
lists are mutable in python
"""
list_one = [10, 24.56, 'sirisha', True]
my_list = []

my_list.append(10)
my_list.append(278.99)
my_list.append('surya')
my_list.append('prakash')
my_list.append(10)

print(list_one)
print(my_list)

print(my_list[0])

list_one[2] = 56
print(list_one)

# two conncatinate two lists we can + operator
list_two = list_one+my_list
print(list_two)

# list slicing
print(list_two[0:4:1])

print(list_two[::-1])

print(list_two[:7:2])

print(list_two[2::3])

# list methods
# get the length of list
print(len(list_two))

# insert() will add data at a given index value
list_two.insert(3, 'sirisha')
print(list_two)

# count() return number of time given object occured
print(list_two.count(10))

# pop() will remove last index value of the given list
print(list_two.pop())
print(list_two)

# remove() will remove a given object from the list
list_two.remove(10)
print(list_two)

# reverse() will reverse the given list
list_two.reverse()
print(list_two)

# list_two.sort()
# print(list_two)

list_three = [12,13,17, 10]

list_three.sort()
print(list_three)


list_two.insert(5, list_three)
print(list_two)

# print(list_two[5][::-1])
list_two[5].reverse()
print(list_two[5])

# clear() will remove all the objects from the list
list_two.clear()
print(list_two)
