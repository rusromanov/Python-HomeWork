# Coding: utf-8

# number = int(input('Введите целое положительное число: '))
number = 12345678987654321
number = str(number)

max_num = 0
for element in number:
    if int(element) > max_num:
        max_num = int(element)

print(f'Самая большая цифра в числе {number} - это {max_num}')
