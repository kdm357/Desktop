"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt


"""

from urllib.request import urlopen


def fetch_words(file):
    """
    fetch words from file
    :return:
    """

# Task #2
from urllib.request import urlopen
data = []
count = 0
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words:
            data.append(word)
    return data


def main():
    """

    :return:
    """

file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
fetch_words(file)


if __name__ == "__main__":
    main()
    exit(0)