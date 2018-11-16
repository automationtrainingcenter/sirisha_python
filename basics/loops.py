"""
loops are used to execute a block of code for certain number of interations

while loop
initialization

while expression:
    statements
    increment or decrement

for loop
it is used to iterated over a collection
for i in collection:
    statements


range(start, end, step):

range does not include end value
for reverse iteration step = -1

"""
# print(value, sep=' ', end='n', file=sys.stdout, flush=False)
# print even numbers until given number
last_number = int(input('enter last number '))

# initialization
i = 0
# expression
while i < last_number:
    if i%2 == 0:
        print(i, end='\t')
    #  increment
    i += 1

print('\n')

for char in 'python with django':
    print(char, end='\t')

for i in range(10, 1, -1):
    print(i, '\t')
