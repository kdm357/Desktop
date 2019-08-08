"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

"""
from airtravel import Flight, Aircraft


def main():
    """
    test function for words library
    :return: nohing
    """
    f = Flight("SN067")
    print(f.number())
    print(f.airline())
    print(f.flight_number())
    # could use Flight.number(f)

    a1 = Aircraft("G-EUP","Airbus A319",num_rows=22,
                  num_seats_per_row=6)
    print(a1.registration())
    print(a1.model())

if __name__ == '__main__':
    main()
    exit(0)