"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

"""
from airtravel import Flight


def main():
    """
    test function for words library
    :return: nohing
    """
    f = Flight("SN067")
    print(f.number())


    # could use: Flight.number(f)


if __name__ == '__main__':
    main()
    exit(0)