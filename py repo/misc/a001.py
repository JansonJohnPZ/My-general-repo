import numpy as np


def pow_for_mod(a, b, group_size):

    temp = 1
    for k in range(b):
        temp = (temp * a) % (group_size + 1)

    return temp


def expand_elem(a, group_size):

    temp_list = []
    for i in range(group_size):
        temp = pow_for_mod(a, i+1, group_size)
        temp_list.append(temp)

    return temp_list


def show_ord_map(group_size):

    array_temp = np.zeros([group_size, group_size], dtype="float64")

    for i in range(group_size):
        for j in range(group_size):
            array_temp[i, j] = pow_for_mod(i+1, j+1, group_size)

    return array_temp


def ord_of_elem(group_size):

    array_temp = show_ord_map(group_size)
    shape_a = array_temp.shape

    temp = []
    for i in range(shape_a[1]):
        temp.append(len(set(array_temp[i, :])))

    return temp


def find_gen(group_size):

    temp = ord_of_elem(group_size)
    temp_list = []

    for i in range(group_size):
        if temp[i] == group_size:
            temp_list.append(i+1)
    return temp_list


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

    group_size = 22                #23

    # array_temp = show_ord_map(group_size)
    # print(array_temp)

    temp_list = []
    for i in range(1, group_size+1):
        temp_list.append(find_reverse(i, group_size))
    print(temp_list)

    # temp = find_reverse(1, group_size)
    # print(temp)

    # temp_list = ord_of_elem(group_size)
    # print(temp_list)

    # temp = find_gen(group_size)
    # print(temp)

    # temp_list = expand_elem(15, group_size)
    # print(temp_list)
    # print(len(temp_list))
    # print(len(set(temp_list)))


if __name__ == "__main__":
    main()

