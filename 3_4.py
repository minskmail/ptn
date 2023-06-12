# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
while 1:
    pos_counter = 0
    neg_counter = 0
    zero_counter = 0
    numlist = []
    for i in range(3):
        numlist.append(float(input('input number: ')))

    for item in numlist:
        if item > 0:
            pos_counter += 1
        elif item < 0:
            neg_counter += 1
        else:
            zero_counter += 1

    print('pos:', pos_counter)
    print('neg:', neg_counter)
    print('zero:', zero_counter)
