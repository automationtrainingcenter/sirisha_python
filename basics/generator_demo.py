"""
Generators in python are very similar to normal functionself. But instead of returning a value
it will suspend the current execution and save the state for next execution.
"""


# normal fucntion
def nor_func(n):
    square_list = []
    for num in range(n):
        square_list.append(num**2)
    return square_list

for num in nor_func(5):
    print(num)

# generator function using yield
def my_gen(n):
    for num in range(n):
        yield num**2

# for squre in my_gen(5):
#     print(squre)


 # febnocii series using normal function
def feb_normal(n):
    i=1
    j=1
    feb_series = []
    for num in range(n):
        feb_series.append(i)
        i, j = j, j+i
    return feb_series

for num in feb_normal(10):
    print(num, end='\t')

print()
# febnocii series using generator function
def feb_gen(n):
    i=1
    j=1
    for num in range(n):
        yield i
        i, j = j, j+i


for num in feb_gen(10):
    print(num, end='\t')
print()

# d = feb_gen(5)
# value = next(d)
# while value is not None:
#     print(value)
#     value =next(d)

s = iter("sirisha")
print(next(s))
