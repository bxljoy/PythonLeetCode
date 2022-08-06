import timeit
import random


def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))

def findLevelK(listnum, k):
    if k > len(listnum):
        return None
    else:
        listnum.sort()
        return listnum[k-1]

if __name__ == '__main__':
    # t1 = timeit.Timer("test1()", "from __main__ import test1")
    # print("concat ", "%10.5f" % t1.timeit(number=1000), "milliseconds")
    # t2 = timeit.Timer("test2()", "from __main__ import test2")
    # print("append ", "%10.5f" % t2.timeit(number=1000), "milliseconds")
    # t3 = timeit.Timer("test3()", "from __main__ import test3")
    # print("comprehension ", "%10.5f" % t3.timeit(number=1000), "milliseconds")
    # t4 = timeit.Timer("test4()", "from __main__ import test4")
    # print("list range ", "%10.5f" % t4.timeit(number=1000), "milliseconds")
    #
    # popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    # popend = timeit.Timer("x.pop()", "from __main__ import x")
    #
    # print("i       pop(0)      pop()")
    # for i in range(1000000, 10000001, 1000000):
    #     x = list(range(i))
    #     pz = popzero.timeit(number=1000)
    #     x = list(range(i))
    #     pe = popend.timeit(number=1000)
    #     print("%d, %10.5f, %10.5f" % (i, pz, pe))

    lst_del_time = 0
    dict_del_time = 0
    for i in range(10000, 1000001, 10000):
        # t = timeit.Timer("x[random.randrange(%d)]" % i, "from __main__ import random, x")
        # x = list(range(i))
        # lst_time = t.timeit(number=1000)
        # print("%d, %10.5f" % (i, lst_time))
        #
        # s = timeit.Timer("y[random.randrange(%d)]" % i, "from __main__ import random, y")
        # y = {j: None for j in range(i)}
        # dict_get_time = s.timeit(number=1000)
        # print("%d, %10.5f" % (i, dict_get_time))
        #
        # r = timeit.Timer("y[random.randrange(%d)] = 1" % i, "from __main__ import random, y")
        # y = {j: None for j in range(i)}
        # dict_set_time = r.timeit(number=1000)
        # print("%d, %10.5f" % (i, dict_set_time))

        d = timeit.Timer("del z[random.randrange(%d)]" % i, "from __main__ import random, z")
        z = list(range(i))
        lst_del_time += d.timeit(number=1)
        z = {j: None for j in range(i)}
        dict_del_time += d.timeit(number=1)
        print("%10.5f, %10.5f" % (lst_del_time, dict_del_time))

    list_num = [4, 56, 12, 47, 1, 98, 69]
    print(findLevelK(list_num, 5))


