n = int(input('Введите верхнюю границу последовательности: '))

num = (n for n in range(1, n+1, 2))
print(*num)
