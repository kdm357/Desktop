"""
Learn about scope in Python

"""
count = 0  # global object


def show_count():
    """
    show current count
    :return:
    """
    print(count)


def set_count(number):
    """

    :param number:
    :return:
    """
    global count
    count = number


def main():
    """
    test function for words library
    :return: nohing
    """
    show_count()
    set_count(30)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)