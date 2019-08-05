"""
Learn condittional repition
Two loops: For loopa and while loops
"""

counter = 5
while counter != 0:
    print(counter)
    # Augmented Operator
    counter -= 1

counter = 5
while counter:
    print(counter)
    # Augmented Operator
    counter -= 1

while True:
    print("Enter a  number")
    response = input()  # take user input
    if int(response) % 7 == 0:
        break           # exit loop


print("outside while loop")