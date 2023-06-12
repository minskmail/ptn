# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные

source_list = [1, 2, 3, 4, 5, 6, 22, 23, 111, 11]


def list_sort(slist):
    slist.sort(key=lambda x: (x % 2 == 1))
    return slist


print(list_sort(source_list))
