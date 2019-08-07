"""
Learn about sets
an unordered collection of unique immutable objects
Define it using {} just like a dictionary
You can use the set() constructor
"""


def main():
    """
    test function for words library
    :return: nohing
    """
    p = {6,78,21,45}
    print(p, type(p))
    data = [1,3,5,2,88,3,1]
    print(data)
    #eliminates duplicates
    sdata = set(data)
    print(sdata)

    #iterate
    for item in sdata:
        print(item)
    print(5 in sdata)
    # add velements to a set
    sdata.add(45)
    print(sdata)
    sdata.update([33,44,55,45,45])
    print(sdata)
    # raises an error if not found
    sdata.remove(88)
    print(sdata)
    # discard does not raise error
    sdata.discard(46)
    print(sdata)

    #copy sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)

    ##### define some sets
    blue_eyes = {"Olivia","Harry","Lilly",'Jack'}
    blonde_hair = {"Harry","Jack","Amelia","Mia","Joshua",}
    smell_hcn = {"Harry","Amelia"}
    taste_ptc = {"Harry","Lilly","Lola"}
    o_blood = {"Joshua","Lola"}
    b_blood = {"Amelia","Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Joshua","Lola"}
    print(blue_eyes.union(blonde_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blonde_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))




if __name__ == '__main__':
    main()
    exit(0)