# Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
iname = input('Input name: ')
iage = input('Input age: ')
icity = input('Input city: ')

print('My name is ' + iname + '. I\'m ' + iage + ' years old from ' + icity)
print('My name is {}. I\'m {} years old from {}'.format(iname, iage, icity))
print(f'My name is {iname}. I\'m {iage} years old from {icity}')
