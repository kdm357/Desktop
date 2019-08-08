"""
generator objects are a cross between comprehensions and generator functions
syntax: similar to list comprehension, but with parameters
(expr(item) for item in iterable)
"""
from list_comprehensions import is_prime

def main():
    """
    test function for words library
    :return: nohing
    """

    # list with first 1 million square numbers
    m_sq = (x*x for x in range(1,1000001))
    print (m_sq, type(m_sq))
    print("The sum of the first 1M squared numbers is: ", sum(m_sq))
    print("The sum of the first 1M squared numbers is: ", sum(x*x for x in range(1,1000000)))

    # the sum of the prime numbers between 1 to 10K
    print("The sum of the first 10K squared numbers is: ", sum(x for x in range(1, 10001) if is_prime(x)))





if __name__ == '__main__':
    main()
    exit(0)