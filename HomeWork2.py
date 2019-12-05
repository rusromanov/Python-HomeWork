# Coding: utf-8

# seconds = int(input('Введите секунды: '))
seconds = 3661

hours = seconds // 3600
mins = (seconds / 60) % 60
sec = seconds % 60

print(f'{seconds} сек. (ЧЧ:ММ:СС) -', '{:>02d}'.format(hours), ':', '{:>02d}'.format(int(mins)), ':', '{:>02d}'.format(int(sec)))
