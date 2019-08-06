"""
Learn about return semantics an dfunction arguments in Python

"""

def print_border(char, length):
    """

    :param char:
    :return:
    """
    print(length)
    counter = length
    while counter > 0:
        print(char)
        counter -= 1




def banner(message, border = "*"):
    '''

    :param message:
    :param border:
    :return:
    '''

    print_border(border,len(message))
    print(message)
    print_border(border, len(message))



def sum_two(num1, num2 = 8):
    """
    Sum two input objects
    :param num1:
    :param num2: optional, default = 8
    :return: sum o fobjects
    """
    return num1 + num2

def egg(var):
    """
    returns the ariable back to the user
    :param var:
    :return:
    """
    return var

def add_spam(menu = None):
    """
    Add Spam to the menu
    :param menu:
    :return: The list
    """
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    """
    test function for words library
    :return: nohing
    """
    c = [6,10,20]
    e = egg(c)
    print(c is e)
    n1 = 3
    n2 = 9
    print(n1, " + ", n2, " = ", sum_two(n1, n2))

    print("Only one input", sum_two(n1))

    banner("Weber State")

    breakfast = ["eggs", "bacon"]
    add_spam(breakfast)
    print ("After", breakfast)




if __name__ == '__main__':
    main()
    exit(0)