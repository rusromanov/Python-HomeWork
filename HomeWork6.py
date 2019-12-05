# Coding: utf-8

# a = int(input("Введите результат 1го дня: "))
# b = int(input("Введите желаемый результат: "))
a = 2
b = 3

day = 1
print(f'{day}-й день {a}')
while True:
    if a < b:
        a = a + (a / 10)
        day += 1
        print(f'{day}-й день', '{:.2f}'.format(a))
        if a >= b:
            print(f'Ответ: на {day}-й день спортсмен достиг рузультата - не менее {int(a)}км.')
            break
