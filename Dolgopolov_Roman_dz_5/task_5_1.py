def gen_odd_num(n):
    for i in range(1, n+1, 2):
        yield i


num = gen_odd_num(int(input('Введите верхнюю границу последовательности: ')))
print(*num)
