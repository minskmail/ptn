# Дан список содержащий в себе различные типы данных, отфильтровать таким образом, чтобы остались только строки,
# использование дополнительного списка незаконно

source_list = [5.1, 'task', 1, 4, True, 'filter']


def fltr_str(lst):
    n = 0
    while n < len(lst):
        if type(lst[n]) != str:
            lst.pop(n)
        else:
            n += 1
    return lst


print(fltr_str(source_list))
