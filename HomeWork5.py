#Coging: utf-8

# proceeds = int(input('Введите выручку фирмы: '))
# costs = int(input('Введите издержки фирмы: '))
proceeds = 1000000
costs = 400000

if proceeds > costs:
    print('Ваша фирма работает в прибыль!')
    profit = proceeds - costs
    print(f'Прибыль: {profit}')
    profitability = (profit / proceeds) * 100
    print(f'Рентабельность: {profitability}%')
    # firm_size = int(input('Введите численность фирмы: '))
    firm_size = 8
    empl_profit = profit / firm_size
    print('Прибыль на одного сотрудника:', '{:.2f}'.format(empl_profit))
else:
    print('Ваша фирма работает в убыток')
    loss = costs - proceeds
    print(f'Убыток: {loss}')
