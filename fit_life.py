# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
LITER_OF_WATER = 1000


# приветствие
print('Здравствуйте! Нам нужно познакомиться, чтобы я стал полезным для Вас.')
print('')

# сбор данных
user_name = input('Напишите свое имя: ')
user_age = int(input('Ваш возраст: '))
user_weight = float(input('Вес в килограммах (например 75.5): '))
user_height = float(input('Рост в метрах (например 1.8): '))
print('__________________________________________')
print('')

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт рекомендуемой нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / LITER_OF_WATER
water_l = round(water_l, 1)

# итоговый отчет
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print('')
print('Расчет окончен. Будьте здоровы!')
