"""
when working with iterators, generators, etc
look at the documentation for the itertools module
"""
from itertools import islice, count
from list_comprehensions import is_prime



def main():
    """
    test function for words library
    :return: nohing
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print ("List of first 1K fprime numbers:", list(thousand_primes))
    # Note: if you need to use the object again, you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first 1K fprime numbers:", sum(thousand_primes))

    # Other build-ins use with itertools: any (OR), all (AND)
    print(any([False, False, True]))
    print(all([False, False, True]))

    print(any(is_prime(x) for x in range(1352, 1360)))


if __name__ == '__main__':
    main()
    exit(0)