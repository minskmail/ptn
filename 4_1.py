# Заполнить список степенями числа 2 (от 2^1 до 2^n).

while 1:
    n_value = int(input('Insert value \'n\': '))
    lst = []
    for i in range(n_value + 1):
        if i > 0:
            lst.append(2**i)
    print(lst)
