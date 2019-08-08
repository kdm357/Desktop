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

    def airline(self):
        return self._number[:2]

    def flight_number(self):
        return self._number[2:]


class Aircraft:

    def __init__(self, registration, model,
                 num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

def main():
    """
    test function for words library
    :return: nohing
    """


if __name__ == '__main__':
    main()
    exit(0)