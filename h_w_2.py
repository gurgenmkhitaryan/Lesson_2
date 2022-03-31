list_str = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
            'была', '-5', 'градусов'
            ]

i = 0
while i < len(list_str):
    try:
        number = int(list_str[i])
    except ValueError:
        i += 1
    else:
        if list_str[i][0] in ('-', '+'):
            list_str[i] = f'{number:+03d}'
        else:
            list_str[i] = f'{number:02d}'
        list_str.insert(i, '"')
        list_str.insert(i + 2, '"')
        i += 3

print(' '.join(list_str))
