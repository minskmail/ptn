# Вывести первые N чисел кратные M и больше K

while 1:
    n_number = int(input('N: '))
    m_number = int(input('M: '))
    k_number = int(input('K: '))

    value = k_number + 1
    counter = 0
    value_list = []

    while counter < n_number:
        if value > k_number and (value % m_number) == 0:
            value_list += [value]
            value += 1
            counter += 1
        else:
            value += 1
    print(value_list)
