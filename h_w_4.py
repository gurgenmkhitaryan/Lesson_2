price_list = [22.2, 31.2, 3.0, 5.4, 2.5, 9.11, 11.9, 6.11, 11.6, 69.6, 66.9]


def price_to_str(price):
    return (f'{int(price)} руб {int(price * 100 % 100):02d} коп')


# А
price_str = ', '.join(map(price_to_str, price_list))
print('Исходный прайс\n', price_str, '\n')

# B
print('Список до сортировки: ', id(price_list))
price_list.sort()
price_str = ', '.join(map(price_to_str, price_list))
print('Список после сортировки', id(price_list))
print(price_str, '\n')

# C
price_list_decr = price_list[::-1]

# D
price_str = ', '.join(map(price_to_str, price_list_decr[:5]))
print('5 самых высоких цен\n', price_str)
