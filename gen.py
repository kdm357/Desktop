"""
Module for demonstration the use of generator execution
"""


def take(count, iterable):
    """
    take items frm the front of an iterable
    :param count: maximum number of items to retrieve
    :param iterable: the source series
    :Yields: at most 'count' item fo r'iterator'
    """

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """
    Test the take() function
    :return:
    """
    items = [2,4,5,8,10]
    for item in take(3, items):
        print(item)


def run_pipeline():
    items = [3,6,6,2,1,1]
    for item in take(3,distinct(items)):
        print(item)


def distinct(iterable):
    """
    return unique item by eliminating duplicates
    :param iterable: the source series
    :yield: unique elements in order from iterable
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5,7,7,6,5,5]
    for item in distinct(items):
        print(item)


def main():
    """
    test function for words library
    :return: nohing
    """
    # run_take()
    # run_distinct()
    run_pipeline()


if __name__ == '__main__':
    main()
    exit(0)