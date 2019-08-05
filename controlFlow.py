"""
Learn about control flow in Python
"""

# If statement
if True:
    print("It is True")

if bool("eggs"):
    print("Yes Please")

if "eggs":
    print("Yes, Why not")


# Flat is better than nested
h=42
if h>50:
    print("Greater than 50")
    if h>100:
        print("Greater than 100")
elif h<50:
    print("Less than 50")
else:
    print("equals 50")

print("Done")