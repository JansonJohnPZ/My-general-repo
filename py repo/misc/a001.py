import numpy as np


def show_ord_map(group_size):

    array_temp = np.zeros([group_size, group_size], dtype="float64")

    for i in range(group_size):
        for j in range(group_size):
            array_temp[i, j] = ((i + 1) ** (j + 1)) % (group_size + 1)

    return array_temp


def find_gen(group_size):
    array_temp = show_ord_map(group_size)
    shape_a = array_temp.shape
    for i in range(shape_a[1]):
        print(i)


def find_reverse_sub0(o, p, k):

    a = p // o
    b = p % o

    if b == 1:
        return -a, 1

    c, d = find_reverse_sub0(b, o, k)

    e = (d - a * c) % k
    f = c % k

    return e, f


def find_reverse(o, p):

    if o == 1:
        return 1

    k = p + 1

    a, b = find_reverse_sub0(o, k, k)
    a = a % k

    return a


def main():

    group_size = 12                 #13

    # array_temp = show_ord_map(group_size)
    # print(array_temp)
    #
    # temp = find_reverse(12, group_size)
    # print(temp)

    find_gen(group_size)


if __name__ == "__main__":
    main()

