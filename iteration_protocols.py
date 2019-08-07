"""
Learn about iterable, iterator objects
use the built-in:
 iter(): create and iterable object
 next(): fetch the next element in the iterable object
"""


def first(iterable):
    """
    return next member in list (if available)
    :param iterable: object
    :return: next member or
    :except: ValueError for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    """
    test function for words library
    :return: nohing
    """
    iterable = ["Sring","Summer","Fall","Winter"]
    iterator = iter(iterable) # give me an iterator
    print(type(iterator), iterator)



if __name__ == '__main__':
    main()
    exit(0)