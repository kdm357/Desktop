"""
Learn about List()

"""


def main():
    """
    test function for words library
    :return: nohing
    """
    s = "show how to do it".split()
    print(s, type(s))

    # access by index
    print(s[3])
    print("last member",s[len(s)-1])

    # use negative index
    print("last member", s[-1])

    # slicing
    print("from 1 to one before last member",s[1:-1])
    print("from 1 to end", s[2:])
    print("from 1 to one to last 3", s[:-3])
    print("from all", s[:])
    # make a copy
    t = s  #shallow copy
    # t = s.copy()
    # t = list(s)
    print("t is s: ",t is s)
    t2 = s[:]  # deep copy
    print("t is S", t2 is s)
    print(t==s)

    # shallow copies
    # a list of list
    a = [[1,2],[3,4]]
    print(a, type(a))
    print(a[0][1])
    # copy the list of list
    b = a[:]

    # modify a[0]
    a[0] = [1,2]
    print (a[0] is b[0])

    # modify a[1]
    a[1].append(5)

    # repitition
    c = [21,37]
    d = c * 4
    print("c", c)
    print("d", d)
    s = [[-1, 1 ]] * 5
    print(s)
    s[1].append(7)
    print(s)

    # index() method
    w = 'the quick brown fox jumps over the lazy dog'.split()
    i = w.index('fox')
    print("The index of 'fox' entry is:", i)

    # if not found throws an exception
    # i = w.index('cat')

    # membership testing with: count()
    print("'the' value is ", w.count("the"))

    # also test membershop with in, not in
    print(37 in [12,22,37,99])
    print(38 not in [12, 22, 37, 99])

    # removing elements from list
    w = 'the quick brown fox jumps over the lazy dog'.split()
    print(w)
    del w[3]   # delete
    print(len(w),w)

    # remove using: remove()
    w.remove("over")
    print(len(w), w)

    # same as
    # del w[w.index["dog"]]
    # print(len(w), w)

    # rearrange list of elements
    g = [1, 34, 5678, 11234]
    print(g)
    # print("reverse",g.reverse())

    d = [12,34,1,78,90]
    print("d:", d)
    d.sort()
    print("sort d:", d)
    d.sort(reverse=True)
    print("sort.reverse d:", d)

    # sort by key
    w = 'the quick brown fox jumps over the lazy dog'.split()
    print(w)
    w.sort(key=len)
    print("sort by key:", w)








if __name__ == '__main__':
    main()
    exit(0)