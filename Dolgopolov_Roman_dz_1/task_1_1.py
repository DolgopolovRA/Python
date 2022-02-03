duration = int(input('Введите промежуток времени в секундах: '))

if duration < 60:
    print(f'{duration} сек')
elif 60 <= duration < 3600:
    print(f'{duration // 60} мин {duration % 60} сек')
elif 3600 <= duration < 86400:
    remains_m_s = duration % 3600  # остаток минут и секунд, занёс в переменную, чтобы не выполнять повторяющуюся
    # арифметическую опеацию
    print(f'{duration // 3600} час {remains_m_s // 60} мин {remains_m_s % 60} сек')
else:
    remains_m_s = duration % 3600  # остаток минут и секунд, занёс в переменную, чтобы не выполнять повторяющуюся
    # арифметическую опеацию
    print(f'{duration // 86400} дн {duration % 86400 // 3600} час {remains_m_s // 60} мин {remains_m_s % 60} сек')
