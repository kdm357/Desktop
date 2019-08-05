"""
get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task#1: count number of words in document
"""

from urllib.request import urlopen


def fetch_words(filename):
    """
    fetch words from file
    :return:
    """

# Task #2
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
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