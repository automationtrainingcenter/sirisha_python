# num_list = []
#
# # creating list from a range function
# for num in range(1, 10):
#     # if num % 2 == 1:
#     #     continue
#     num_list.append(num)

num_list = [num for num in range(1,10)]
print(num_list)

# square of a range of numbers
list2 = [num ** 2 for num in range(1,10)]
print(list2)

# square of even numbers
square_of_even_numbers = [num ** 2 for num in range(1, 10) if num %2 == 0]
print(square_of_even_numbers)

genders = [1, 0, 0, 0, 1, 1, 1, 0, 1]
gender_list = ['Male' if num == 1 else 'Female' for num in genders]
print(gender_list)
