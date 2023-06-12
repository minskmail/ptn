# Пользователь вводит 3 числа, найти среднее арифметическое с точностью 3
numa = input('enter number 1: ')
numb = input('enter number 2: ')
numc = input('enter number 3: ')

average_sum = (float(numa) + float(numb) + float(numc))/3

print(round(average_sum, 3))

