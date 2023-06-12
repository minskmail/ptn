# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

while 1:

    def calculate(num, operator, num2):
        if operator == '+':
            return num + num2
        elif operator == '-':
            return num - num2
        elif operator == '*':
            return num * num2
        elif operator == '/':
            return num / num2
        else:
            raise ValueError('Operator not allowed, please select from list: +-*/')


    num = float(input('Insert number: '))
    operator = input('Input operator: ')
    num2 = float(input('Insert second number: '))
    result = calculate(num, operator, num2)
    print('Result: {}'.format(result))
