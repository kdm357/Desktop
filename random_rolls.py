"""
simulate 6000 rolls of a die (1-6)

"""
import random
import statistics

def roll_die(num):
    """
    random roll of die
    :param num: number of rolls
    :return: a list of frequencies
    """
    freq = [0] * 6  # initial value

    for roll in range(num):
        n = random.randrange(1,7)
        freq[n-1] += 1
    return freq

def main():
    """
    test function for words library
    :return: nohing
    """
    num = int(input("how many times you need to roll"))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print(roll, total)

    print("average = {}".format(sum(result) / len(result)))
    print("mean = {}".format(statistics.mean(result)))
    print("median = {}".format(statistics.median(result)))

if __name__ == '__main__':
    main()
    exit(0)