"""
Learn more about strings

"""


def main():
    """
    test function for words library
    :return: nohing
    """
    s1 = "This is super cool"
    print("Size of S1: ", len(s1))
    #concatenation
    s2 = "Weber" + "State" + "University"
    print(s2)
    # to join large strings use join
    teams  = ["Real Madrid","Barcelona","Manchester United"]
    record = ":".join(teams)
    # print (record)
    # Split record
    print(record.split(":"))
    # partitioning strings
    # you can use the dummy object ("_")
    departure, _, arrival = "London:Edinburg".partition(":")
    print(departure, arrival)
    # String formatting using format method
    print("The age of {0} is {1}".format("Mario", 34))
    #ommiting the index
    print("The best numbers are {} and {}".format(4,22))
    # or by fieldname
    print("Current position {latitude} {longitude}".format(latitude="60 N", longitude="5 E"))


if __name__ == '__main__':
    main()
    exit(0)