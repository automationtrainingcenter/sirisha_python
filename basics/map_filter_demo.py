"""
map and filter are functions which accepts another function as an argument
"""

def is_even(num):
    if(num % 2 == 0):
        return num

num_list = [1, 2, 3, 5, 4, 8, 9, 12, 21, 33, 13, 6]
# even_list = []
#
# for num in num_list:
#     if num % 2 ==0:
#         even_list.append(num)

# even_list = [num for num in num_list if num %2 == 0]
# filter function returns filtered data based on given condition on a sequence
filtered_data = filter(is_even, num_list)

print(type(filtered_data))

even_list = list(filtered_data)

print(even_list)


def high_salary(employee):
    print(type(employee))
    if employee[1] >= 10000:
        return employee[0]

def name_length(employee):
    if len(employee[0]) >= 5:
        return employee[0]



names_list = ['surya', 'sirisha', 'john', 'jade', 'ram']
salaries_list = [10000, 8000, 12000, 11000, 9000]
employee_list = list(zip(names_list, salaries_list))
high_salary_employees = list(filter(lambda employee : employee[1] >= 10000 , employee_list))
print(high_salary_employees)
print(list(filter(lambda employee : len(employee[0]) >= 5, employee_list)))

def add(a, b):
    return a+b

# result = add(10, 20)
result = lambda a,b : a+b
print(add(result(10, 20), 30))

# map function performs operation on every element of the sequence
map_list = [1,2,3,4,5]

print(list(filter(lambda x : x%2 == 0 , map_list)))
print(list(map(lambda x : x%2==0, map_list)))

# dictionar comprehension
# python old versions
emp_dict = {k:v for k,v in zip(names_list, salaries_list)}
print(emp_dict)
print(type(emp_dict))

# python new version from 3.6
print(dict(zip(names_list, salaries_list)))
