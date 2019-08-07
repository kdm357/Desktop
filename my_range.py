"""
Learn about Range collection
"""


def main():
    """
    test function for words library
    :return: nohing
    """
    for i in range(5):
        print(i)

    # set the initial value
    for i in range(5,10):
        print(i)

    # create a list from a range
    l = list(range(5,10))
    print(l, type(l))

    # multiple ranges
    l2 = list(range(5, 10)) + list(range(30,40))
    print(l2, type(l2))

    # step argument
    l3 = list(range(0, 20, 2))
    print(l3, type(l3))

    #
    s = [0,2,3,4,6]
    for i in range(len(s)):
        print(s[i])


    # better way
    for v in s:
        print(v)

    # enumerate(): returns a iterable series
    t=[6,789,123,98,3,22]
    for p in enumerate(t):
        print(p)

    # a better way
    for i, v in enumerate(t):
        print(i,v)



if __name__ == '__main__':
    main()
    exit(0)