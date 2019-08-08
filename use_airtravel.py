"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def main():
    """
    test function for words library
    :return: nohing
    """
    f1 = Flight("SN067",Aircraft("G-EUP","Airbus A319",num_rows=22,
                  num_seats_per_row=6))

    pp(f1._seating)

if __name__ == '__main__':
    main()
    exit(0)