"""
this program explains strings in Python
"""

str1 = "python with Django"
str2 = 'welcome to the course Sirisha'

str3 = "12324"

print(str1+str2)
print(len(str1))
print(str1[10])
print(str1[len(str1)-1] )
print(str1[-1])

# slicing str[start : end : step]
# default step value is 1 and ending index value does not include
print(str1[0 : 8])
print(str1[10:]) # from index 10 to len
print(str2[:16]) # from index 0 to 15
print(str1[:]) #complete string
print(str1[::-1]) # reverse of the string
print(str1[2:10:2]) # to i
print(str1[::2]) #values at even index
print(str1[1::2]) # values at odd index

# string methods
print(str1.capitalize())
print(str1.lower())
print(str1.title())
print(str1.upper())

if str2.isnumeric():
    print(int(str2))

print(type(str2.split(" ")))
print(str2.split(' '))

print(''.join([str1,' ',str2]))

print(str1 == '')
