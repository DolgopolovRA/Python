# Решение задачи включает задание со *, не создавая новый список

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
result_str = ''

# обособление чисел в кавычки

while index < len(list_1):
    elem = list_1[index]
    number = 0  # признак что это число
    len_number = 0  # длина числа
    sign = 0  # признак числа со знаком
    for i in range(len(elem)):
        if 48 <= ord(elem[i]) <= 57:
            number = 1
            len_number += 1
        elif i == 0 and (ord(elem[i]) == 43 or ord(elem[i]) == 45):
            sign = 1
        else:
            number = 0
            break
    if number:
        if len_number < 2:
            if sign:
                list_1[index] = elem[0] + '0' + elem[1]
            else:
                list_1[index] = '0' + elem
        # здесь появилась идея сформировать итоговую строку параллельно с формированием списка, но как мне показалось
        # это не соответсвует условию задачи, поэтому закомментировал и сделал циклом после формирования списка

        # result_str += '"' + list_1[index]
        list_1.insert(index, '"')
        list_1.insert(index + 2, '"')
        index += 2
    else:
        # result_str += elem
        # result_str += ' '
        index += 1

# формирование строки из списка

index = 0

while index < len(list_1):
    if list_1[index] == '"':
        result_str += '"' + list_1[index + 1] + '" '
        index += 3
    else:
        result_str += list_1[index] + ' '
        index += 1
    if index > len(list_1):
        break

print(list_1)  # вывод сформированного списка для контроля
print(result_str)  # вывод результирующей строки
