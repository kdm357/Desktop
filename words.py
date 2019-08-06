"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt


"""

from urllib.request import urlopen


def fetch_words(file):
    """
    fetch words from file
    :return: data
    """

    data = []
    count = 0
    with urlopen(file) as story:
        for line in story:
            words = line.decode('utf-8').split()
            for word in words:
                data.append(word)
        return data



def print_items(items):
    """

    :param items:
    :return:
    """
    for item in items:
        print(items)

def main():
    """
    test function for words library
    :return: nohing
    """

    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    info = fetch_words(file)
    print_items (info)


if __name__ == '__main__':
    main()
    exit(0)