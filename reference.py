"""
Learn about references
"""
def modify(k):
    """
    Modify the content of a list
    :return: nothing
    """
    # list is passed by reference (by default)
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    replace input list
    :param g:
    :return:
    """
    g = [17,40,89]
    print("g = ", g)


def replace_contents(g):
    """
    Replace contents of the list
    :param g: list
    :return: nothing
    """
    g[0] = "89"
    g[1] = "22"
    g[2] = "44"
    print("g = ", g)

def main():
    """
    test function
    :return: nohing
    """
    m = [9,15,24]
    print("Before modify m = ", m)
    modify(m)
    print("After modify m = ", m)
    replace(m)
    print("After replace m = ", m)
    replace_contents(m)
    print("After replace_contents m = ", m)



if __name__ == '__main__':
    main()
    exit(0)