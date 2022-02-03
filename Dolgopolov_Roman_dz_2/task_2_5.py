# задание А

prices = [12, 34.1, 9812, 67.9, 123.45, 87, 82.52, 45.23, 39.12, 752, 901, 119.11, 66.04, 911.09]

for i in prices:
    if isinstance(i, int):
        if len(prices) - prices.index(i) != 1:
            print(f'{i} руб 00 коп,', end=' ')
        else:
            print(f'{i} руб 00 коп')
    else:
        r, k = str(i).split('.')
        if len(k) < 2:
            k += '0'
        if len(prices) - prices.index(i) != 1:
            print(f'{r} руб {k} коп,', end=' ')
        else:
            print(f'{r} руб {k} коп')

# задание В

print(id(prices))
prices.sort()
print(prices)
print(id(prices))  # убеждаемся, что новый список не создан

# задание С

new_prices = sorted(prices, reverse=True)
print(new_prices)
print(id(new_prices))  # убеждаемся, что создан новый список

# задание D

print(new_prices[:5])
