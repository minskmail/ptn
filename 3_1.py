# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
init_str = input('Input string: ')

# case 1
print(init_str.replace(' ', '-'))
# case 2
print(f"{'-'.join(init_str.split(' '))}")
