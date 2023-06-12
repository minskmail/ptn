# Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число,
# пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

while 1:
    source_list = input('input numbers separated by commas: ')

    num_list = source_list.split(",")
    num_list = [int(num) for num in num_list]
    num_list_len = len(num_list)

    n_number = int(input(f'input n value in range from 0 to {num_list_len}: '))


    def list_offset(slist, num):
        # N = N % len(lst)  # учитываем случай, когда N может быть больше длины списка
        return slist[-num:] + slist[:-num]


    # result
    print(list_offset(num_list, n_number))
