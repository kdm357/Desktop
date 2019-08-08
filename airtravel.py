"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt


"""

class Flight:
    """
    """
    def __init__(self, number):
        # implementation details begin with '_'
        # validate flight number
        # 5 chars long: AAddd A-> Alpha, d-> digits
        self._number = number

        if len(number) != 5:
            raise ValueError("Invalid Flight number length".format(number))
        if not number[:2].isalpha():
            raise ValueError("No Airlline Code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid Airlline Code {}".format(number))
        if not number [2:].isdigit():
            raise ValueError("Invalid Route Code {}".format(number))


        self._number = number


    def number(self):
        return self._number



def main():
    """
    test function for words library
    :return: nohing
    """




if __name__ == '__main__':
    main()
    exit(0)