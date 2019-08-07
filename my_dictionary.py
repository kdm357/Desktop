"""
Learn about dictionaries
"""

from pprint import pprint as pp

def main():
    """
    test function for words library
    :return: nohing
    """
    urls = {"google": "www.google.com",
            "yahoo":"www.yahoo.com",
            "twitter": "www.twitter.com"}
    print(urls)
    print(urls["google"])

    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)
    print(d)

    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)

    # copy a dictionary
    e = phonetic.copy()
    print(e)

    # updating a dictionary: update()
    stock = {'GOOG':891, "AAPL":416, 'IBM':194}
    print(stock)
    stock.update({'GOOG':999, 'YHOO':2})
    print(stock)

    # iteration
    for val in stock.values():
        print("val = ", val)
    for item in stock.items():
        print(item)

    for key, value in stock.items():
        print(key, value)

    #  Test for membership
    print("GOOG" in stock)
    print("WINDOWS" in stock)

    # deleting
    del stock['YHOO']
    print (stock)

    # mutabillity of dictionaries
    isotopes = {
        'H':[1,2,3],
        'He':[3,4],
        'Li':[6,7],
        'Be':[7,9,10],
        'B':[10,11],
        'C':[11,12,13,14]
    }
    pp(isotopes)
    isotopes['H'] += [4,5,6,7]
    pp(isotopes)
    isotopes['N'] = [13,14,15]
    pp(isotopes)







if __name__ == '__main__':
    main()
    exit(0)