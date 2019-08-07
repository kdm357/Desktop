"""
list comprehensions:
Readible, expressive, and efective.
"""
from math import factorial, sqrt
from pprint import pprint as pp


 # filter predicate
def is_prime(num):
    """
    check for prime

    :param num:  number
    :return: True if prime else False
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) +1 ):
        if num % i == 0:
            return True


def main():
    """
    test function for words library
    :return: nohing
    """
    words = "Today I am very happy to learn about comprehensions".split()
    print(words)
    data = []  #empty list
    for word in words:
        # some analysis
        data.append(word)

    # filter data
    # print(data)

    # task: find the length of the first 20 factorial numbers
    info = []
    for x in range(20):
        info.append(len(str(factorial(x))))
    print(info, type(info))

    # use a comprehension: []
    info2 = [len(str(factorial(x))) for x in range(20)]
    print(info2, type(info2))

    # set comprehension ()
    info3 = {len(str(factorial(x))) for x in range(200)}
    print(info3, type(info3))

    # dictionary comprehension
    nba_teams = {
        'Jazz':'SLC',
        'warriors':'OAKLAND',
        'Lakers':'LA',
        'Clipppers':'LA'
    }
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    print(is_prime((2)))

    # Filter predicates
    primes = [x for x in range(100001) if is_prime(x)]
    pp(primes)




if __name__ == '__main__':
    main()
    exit(0)