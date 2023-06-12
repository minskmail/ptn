# Дан список чисел, необходимо его развернуть без использования метода reverse и функции reversed,
# а так же дополнительного списка и среза


source_list = [1, 2, 3, 4, 5]


def rev_list(slist):
    for n in range(len(slist)):
        slist.insert(n, slist.pop())
    return slist


print(rev_list(source_list))
