"""
Learn about lists
unlike strings, lists are mutable.
you can update, and append elements to it
"""

l = [1,2,3]
print (l, type(l))

# a list of objects (any type)
a = ["aple", "Orange", "pear"]
print(a, a[1])

# replace an element
a[0] = "tomatoes"
print (a, a[1])

#begin with empty list
names = []
counter = 0
while counter < 3:
    s = input("Enter data")
    names.append(s)
    counter = counter + 1
print (names)