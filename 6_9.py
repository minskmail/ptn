# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение - словарь с данными о пользователе
# (имя, фамилия, телефон, почта), вывести имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)


source_dictionary = {
    1: {'name': 'Viachaslau', 'surname': '', 'phone': '375447000000'},
    2: {'name': 'Sasha', 'surname': '', 'phone': '375447000001', 'email': 'sasha@gmail.com'},
    3: {'name': 'Tanya', 'surname': '', 'phone': '375447000002', 'email': ''}
}


def check_mail(dictionary):
    for user_id, user_data in dictionary.items():
        if not user_data.get('email'):
            print(user_data['name'])


check_mail(source_dictionary)
