"""
Learn about collections
Tuples, strings, range, list, dictionaries, sets

"""


def do_tuples():
    """
    practice tuples
    :return:
    """
    #immutable sequenct of aribiraty objects
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size: ",len(t))
    print("One member", t[0])
    # to iterate
    for item in t:
        print(item)

    # single tuple must end with comma
    t1 = (6,)
    print(t1, type(t1))
    #another way to create tuples () are optional
    t2 = 1,2,3,5
    print(t2, type(t2))
    # tuple constructor: tuple()
    t_from_l = tuple([3,77,11])
    print (t_from_l, type(t_from_l))
    # test for membership
    print(5 in (3,6,8,5,12))


def min_max(items):
    """
    return min/max of list
    :param items: tuple
    :return: min/max
    """
    return min(items), max(items)


def swap(v1, v2):
    """
    swap 2 values
    :param v1:
    :param v2:
    :return:
    """
    return v2, v1


def main():
    """
    test function for words library
    :return: nohing
    """
    do_tuples()
    output = (min_max([56,76,12,90]))
    print(output[0])
    print(output[1])
    # tuple unpacking
    lower, upper = (min_max([56, 76, 12, 90]))
    print(lower)
    print(upper)

    a, b = swap(4,2)
    print (a, b)
    a, b = b, a
    print(a, b)




if __name__ == '__main__':
    main()
    exit(0)