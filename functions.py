"""
Learn about functions/definitions
use the keyword: def <name>();
"""


def even_or_odd(number):
    """
    Find i fnumber is even or odd
    print "even" on even numbers
             "odd" on odd numbers
    :param number: input number
    """
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


def main():
    """

    :return:
    """

# Call function
print(__name__)
even_or_odd(43)
even_or_odd(26)

if __name__ == "__main__":
    main()
    exit(0)