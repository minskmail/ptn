# **Вывести четные числа от 2 до N по 5 в строку

n_number = int(input('n: '))
count = 0
for n in range(2, n_number+1, 2):
    print(n, end=" ")
    count += 1
    if count == 5:
        count = 0  # reset counter
        print("\n")

