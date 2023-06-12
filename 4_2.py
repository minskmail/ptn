# Без использования collections, написать программу, которая будет создавать словарь для подсчитывания количества
# вхождений каждой буквы в текст введенный с клавиатуры

while 1:
    sequence = input('Enter you text here: ')

    lst_sequence = list(sequence)
    seq_list = []

    for symbol in lst_sequence:
        if symbol != ' ':
            sym_counter = lst_sequence.count(symbol)
            sym_list = [[symbol, sym_counter]]
            seq_list += sym_list
    seq_dict = dict(seq_list)
    print(seq_dict)


