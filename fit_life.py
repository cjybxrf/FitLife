# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
LITER_OF_WATER = 1000


def main():
    """Вычисляет индекс массы тела (ИМТ)."""
    # приветствие
    print('Здравствуйте! Давайте знакомиться ради вашего блага!\n')

    # узнаем имя
    while True:
        user_name = input('Напишите свое имя: ')
        if user_name:
            break
        print('Пожалуйста, введите имя.\n')

    # узнаем возраст
    while True:
        try:
            user_age = int(input('Ваш возраст: '))
            break
        except ValueError:
            print('Введите целое число (например, 25).\n')

    # узнаем вес
    user_weight = float(input('Вес в килограммах: ').replace(',', '.'))

    # узнаем рост
    user_height = float(input('Рост в метрах: ').replace(',', '.'))
    print('__________________________________________\n')

    # расчёт индекса массы тела
    bmi = user_weight / (user_height ** 2)
    bmi = round(bmi, 1)

    # расчёт рекомендуемой нормы воды
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / LITER_OF_WATER
    water_l = round(water_l, 1)

    return user_name, user_age, bmi, water_l


if __name__ == '__main__':
    user_name, user_age, bmi, water_l = main()

    # итоговый отчет
    print(
        f'Отчет для пользователя: {user_name} ({user_age} г.)\n'
        f'Ваш Индекс Массы Тела: {bmi}\n'
        f'Рекомендуемая норма воды: {water_l} л. в день\n\n'
        'Расчет окончен. Будьте здоровы!\n',
    )
