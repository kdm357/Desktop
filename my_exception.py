"""
Learn about exceptions
"""
import sys

def convert(s):
    """
    convert string to integer
    :param s:
    :return:
    """

    try:
        x = int(s)
        return int(x)
    except (ValueError,TypeError) as e:
        print("conversion error {}" \
              .format(str(e)),file=sys.stderr)

    return -1


def sqrt(x):
    """
    compute sqrt using method of ....
    :param x:  number to compute
    :return: sqrt
    :raise ValueError on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()

    return guess


def main():
    """
    test function for words library
    :return: nohing
    """
    # print(convert("11"))
    # print(convert("11"))
    # print(convert("Hello"))
    # print(convert([1,4,8]))
    try:
        print(sqrt(-1))
    except ValueError:
        print("count not compute the value of negative numbers")

    print("Done")


if __name__ == '__main__':
    main()
    exit(0)