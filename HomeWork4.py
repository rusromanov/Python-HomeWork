# Coding: utf-8

# number = int(input('Введите целое положительно число: '))
number = 12345678987654321
number = str(number)

max_num = int(number[0])
i = 1
while i < len(number):
    if max_num <= int(number[i]):
        max_num = int(number[i])
        i += 1
    elif max_num > int(number[i]):
        i += 1
print(f'Самая большая цифра в числе {number} - это {max_num}')
