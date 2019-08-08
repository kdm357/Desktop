"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    f1ight = Flight("SN067", Aircraft("G-EUP", "Airbus A319", num_rows=22,
                                  num_seats_per_row=6))

    # pp(f1._seating)

    f1ight.allocate_seat("02A", "Guido Van Rossum")
    f1ight.allocate_seat("12B", "rasmus Lefdorf")
    f1ight.allocate_seat("15F", "Bjare Stroustrup")
    f1ight.allocate_seat("03A", "Yudihiro Matsumoto")
    return f1ight


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "| Fllight: {1}" \
             "| Seat: {2}" \
             "| Aircraft: {3}" \
             "|".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '/n'.join(lines)
    print(card)
    print()


def main():
    """
    test function for words library
    :return: nohing
    """
    flight1 = make_flight()
    pp(flight1._seating)
    print("",flight1.num_available_seats())
    flight1.make_boarding_pass(console_card_printer())

if __name__ == '__main__':
    main()
    exit(0)