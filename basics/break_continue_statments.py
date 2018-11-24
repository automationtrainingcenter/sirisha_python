"""
break statement will terminate entire loop
continue statement will skip current iterataion and executes next
"""
num_list = list(range(0,10))

# creating list from a range function
# for num in range(1, 10):
#     if num % 2 == 1:
#         continue
#     num_list.append(num)

print(num_list)


"""
read a string from the console. If it is numeric then add that string to the list
and make sure you add 10 elements in list_two
"""

new_list = []
while True:
    if len(new_list) == 10:
        break
    else:
        input_string = input("enter a string\t")
        if input_string.isnumeric():
            new_list.append(input_string)
        else:
            continue

print(new_list)
