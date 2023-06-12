# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

dec_number = int(input('n: '))

dbinary = bin(dec_number)
print(dbinary)


def bin_to_dec(binary):
    decimal = 0
    for i in range(len(binary)):
        digit = binary[i]
        if digit == '1':
            decimal += 2**(len(binary)-i-1)
    return decimal


print(bin_to_dec(dbinary))
