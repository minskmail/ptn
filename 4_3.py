# *Заполнить словарь где ключами будут выступать числа от 0 до n, а значениями вложенный словарь с ключами "name" и
# "email", а значения для этих ключей будут браться с клавиатуры

while 1:
    n_value = int(input('enter n value: '))
    temp_list = []
    for i in range(n_value + 1):
        temp_list += [[i, {'name: ': input('name : '), 'email:': input('email : ')}]]
    final_dict = dict(temp_list)
    print(final_dict)
