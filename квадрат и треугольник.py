while True:
    ask = input(f'Какую фигура вы хотите посчитать?\n')
    if ask == 'Квадрат':
        choise = input(f'Что считаем? Периметр или Площадь?\n')
        if choise == 'Периметр':
            storona = int(input('Введите длинну стороны квадрата\n'))
            print(f'Периметр квадрата равен {storona * 4}')
            break
        elif choise == 'Площадь':
            storona = int(input('Введите длинну стороны квадрата\n'))
            print(f'Площадь квадрата равна {storona * 2}')
            break
        else:
            print(f'Ошибка, проверьте введенные данные!')
    elif ask == 'Прямоугольник':
        choise = input(f'Что считаем? Периметр или Площадь?\n')
        if choise == 'Периметр':
            storona = int(input('Введите длинну стороны прямоугольник\n'))
            storona_2 = int(input('Введите ширину стороны прямоугольник\n'))
            print(f'Периметр прямоугольника равен {(storona * 2)+(storona_2 * 2)}')
            break
        elif choise == 'Площадь':
            storona = int(input('Введите длинну стороны прямоугольника\n'))
            storona_2 = int(input('Введите ширину стороны прямоугольник\n'))
            print(f'Площадь прямоугольника равна {storona * storona_2}')
            break
        else:
            print(f'Ошибка, проверьте введенные данные!')
    else:
        print(f'Такой фигуры нет')



