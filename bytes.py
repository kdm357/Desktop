"""
learn about bytes
bytes are similar to str type, but they are a sequence of
bytes instead of unicode code points

use for raw binary data, fixed-width, single byte endocin: ASCII

Use the byte() constructor
"""

d = b'data'
print (d,type(d))

info = b'some bytes here'
#split the byte using split() method for bytes
print(info.split())


# encoding
message = "Vamos al zool"
data = message.encode("utf-8")
print (data)

new_message = data.decode("utf-8")
print(new_message)