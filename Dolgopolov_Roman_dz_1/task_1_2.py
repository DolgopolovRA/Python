# задание 'а'

cube_list = []
sum_list = 0

for i in range(0, 1000):
    if i % 2 != 0:
        cube_list.append(i ** 3)

for element in cube_list:
    sum_elements = 0
    cycle_element = element
    while cycle_element / 10 > 0:
        sum_elements += cycle_element % 10
        cycle_element = cycle_element // 10
    if sum_elements % 7 == 0:
        sum_list += element

print(sum_list)

# задание 'b', включает решение 'с', не создавая нового списка

index = 0
sum_list = 0

for element in cube_list:
    cube_list[index] = element + 17
    sum_elements = 0
    cycle_element = cube_list[index]
    while cycle_element / 10 > 0:
        sum_elements += cycle_element % 10
        cycle_element = cycle_element // 10
    if sum_elements % 7 == 0:
        sum_list += cube_list[index]
    index += 1

print(sum_list)
