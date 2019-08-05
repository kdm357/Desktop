"""
Strings and Collections

A string is an immutable sequence of Unicode code-poinnts
"""

print ('This is a string')
print ("This is a string too")

#concatenation and adjacent strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

# multiline strings
s3 = """This is
a multiline
string"""
print(s3)

s4 = "This is\na multiple-line\nString"
print(s4)

# support fo rbackslash
s5 = "A\\in a string"
print(s5)

# raw strings
raw_string = r'c:\user\documents\books'
print(raw_string)

# string as sequesnce
s = "parrot"
print("s[4]", s[4], type(s))

print (s.capitalize())
